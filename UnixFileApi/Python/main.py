from abc import ABC, abstractmethod
import os
from datetime import datetime, timedelta
import json

class FileFilter(ABC):
    @abstractmethod
    def matches(self, file_path :str) -> bool:
        pass


class NameFilter(FileFilter):
    def __init__(self, pattern : str):
        self.pattern = pattern
    
    def matches(self, file_path : str):
       filename = os.path.basename(file_path)
       return self.pattern in filename


class DateFilter(FileFilter):
    def __init__(self, days_old : int):
        self.days_old = days_old
        self.cut_off = datetime.now() - timedelta(days = self.days_old)
    
    def matches(self, file_path : str):
        last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
        return last_modified >= self.cut_off

class SizeFilter(FileFilter):
    UNIT_MAP = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3}
    def __init__(self, min_size, max_size = float('inf'), unit = 'B'):
        self.unit = unit
        self.min_size = min_size  * self.UNIT_MAP[unit]
        self.max_size = max_size  * self.UNIT_MAP[unit]
    
    def matches(self, file_path : str):
        size = os.path.getsize(file_path)
        return self.min_size <= size <= self.max_size

class ContentFilter(FileFilter):
    def __init__(self, keyword : str):
        self.keyword = keyword
    
    def matches(self, file_path : str):
        try:
            with open(file_path, "r") as f:
                return any(self.keyword in line for line in f)
        except Exception:
            return False

class CompositeFilter(FileFilter):
    def __init__(self, filter1 : FileFilter, operator: None, filter2 : None):
        self.filter1 = filter1
        self.operator = operator
        self.filter2 = filter2
    
    def matches(self, file_path : str):
        if self.operator == 'AND':
            return self.filter1.matches(file_path) and self.filter2.matches(file_path)
        elif self.operator == 'OR':
            return self.filter1.matches(file_path) or self.filter2.matches(file_path)
        elif self.operator == 'NOT':
            return not self.filter1.matches(file_path)
        return self.filter1.matches(file_path)

class OutputFormatter:
    def __init__(self, format_type = 'Plain'):
        self.format_type = format_type
    
    def format(self, results):
        if self.format_type == 'json':
            return json.dumps(results, indent = 4)
        elif self.format_type == 'csv':
            return "\n".join(results)
        return "\n".join(results)


class FileSearcher:
    def __init__(self, root_dir :str, filters = None):
        self.root_dir = root_dir
        self.filters = filters if filters else []
    
    def search(self):
        matched_files = []

        for root, _ , files in os.walk(self.root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # matched_all_filters = True
                # for f in self.filters:
                #     if not f.matches(file_path):
                #         matched_all_filters = False
                #         break
                # if matched_all_filters:
                #     matched_files.append(file_path) 
                if all(f.matches(file_path) for f in self.filters):
                    matched_files.append(file_path)
        
        return matched_files


#create filters first
size_filter = SizeFilter(min_size=0, unit = 'B')
name_filter = NameFilter('.')
date_filter = DateFilter(3)
content_filter = ContentFilter("this ")

advanced_filter = CompositeFilter(name_filter, 'AND', CompositeFilter(name_filter, 'OR', content_filter))

file_searcher = FileSearcher('/Users/rajrah/Documents/LocalCode/ObjectOrientedDesigns/UnixFileApi/Python',filters=[advanced_filter])
result = file_searcher.search()
formatter = OutputFormatter(format_type="plain")
print(formatter.format(result))


