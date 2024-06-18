# Parent-Child-CSV

This repository contains a Python script to handle a parent CSV file (`housing.csv`) and create multiple child CSV files from it, each containing different columns. It supports both manual updates and automated updates using the `watchdog` library to reflect changes from the parent CSV to the child CSVs in real-time.

## Repository Link

[Parent-Child-CSV](https://github.com/sgindeed/Parent-Child-CSV)

## Introduction

This project demonstrates how to manage a parent CSV file and create multiple child CSV files with different columns from the parent file. It also shows how to reflect updates in the parent CSV to the child CSVs automatically.

## Prerequisites

- Python 3.x
- pandas
- watchdog (for automation)

To install the required libraries, run:

```sh
pip install pandas watchdog
```

## Manual Update

In manual update mode, you can manually update the `housing.csv` file, and then run the script to propagate the changes to the child CSV files.

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/sgindeed/Parent-Child-CSV.git
    cd Parent-Child-CSV
    ```

2. Ensure you have the required libraries installed:

    ```sh
    pip install pandas
    ```

3. Modify the `housing.csv` file as needed.

4. Run the script to update the child CSVs:

    ```sh
    python manual_update_script.py
    ```

## Automated Update

In automated update mode, the script monitors the `housing.csv` file for any changes and automatically updates the child CSV files whenever the parent file is modified.

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/sgindeed/Parent-Child-CSV.git
    cd Parent-Child-CSV
    ```

2. Ensure you have the required libraries installed:

    ```sh
    pip install pandas watchdog
    ```

3. Run the script to start the watcher:

    ```sh
    python automated_update_script.py
    ```

4. Modify the `housing.csv` file. The changes will be detected and propagated to the child CSVs automatically.

## Usage

1. **Cloning the Repository**:
    - Clone the repository to your local machine using:

    ```sh
    git clone https://github.com/sgindeed/Parent-Child-CSV.git
    cd Parent-Child-CSV
    ```

2. **Installing Required Libraries**:
    - Install the required libraries using pip:

    ```sh
    pip install pandas watchdog
    ```

3. **Manual Update**:
    - Modify the `housing.csv` file manually.
    - Run the manual update script:

    ```sh
    python manual_update_script.py
    ```

4. **Automated Update**:
    - Run the automated update script to start watching for changes:

    ```sh
    python automated_update_script.py
    ```

    - Modify the `housing.csv` file. The changes will be detected and the child CSV files will be updated automatically.

## License

This project is not licensed.
```

This README provides a detailed overview and step-by-step instructions for using both the manual and automated update features of the project.
