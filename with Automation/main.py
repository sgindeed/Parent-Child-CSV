!pip install watchdog

import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

parent_csv_path = '/content/housing.csv'

child_columns = {
    'child1.csv': ['longitude', 'latitude'],
    'child2.csv': ['housing_median_age', 'total_rooms'],
    'child3.csv': ['total_bedrooms', 'longitude'],
    # Add more child CSV definitions here if needed
}

def update_child_csvs(parent_csv_path, child_columns):
    parent_df = pd.read_csv(parent_csv_path)
    
    for child_csv, columns in child_columns.items():
        if all(col in parent_df.columns for col in columns):
            child_df = parent_df[columns]
            child_df.to_csv(child_csv, index=False)
        else:
            print(f"One or more columns in {columns} are not in the parent CSV")

update_child_csvs(parent_csv_path, child_columns)


class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_modified(event):
        if event.src_path.endswith("housing.csv"):
            print(f"{event.src_path} has been modified")
            update_child_csvs(parent_csv_path, child_columns)


if __name__ == '__main__':
  time.sleep(2)  # Delay to simulate timing of modification

  parent_df = pd.read_csv(parent_csv_path)
  parent_df.at[0, 'longitude'] = -122.28

  parent_df.to_csv(parent_csv_path, index=False)
  print("Simulated modification of housing.csv")

  update_child_csvs(parent_csv_path, child_columns)

  watcher = Watcher()
  watcher.run()


child1_df = pd.read_csv('child1.csv')
print(child1_df)
child2_df = pd.read_csv('child2.csv')
print(child2_df)
child3_df = pd.read_csv('child3.csv')
print(child3_df)
