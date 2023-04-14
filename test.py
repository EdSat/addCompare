import csv

def compare_csv_files(file1, file2, output_file):
    """
    Vergleicht zwei CSV-Dateien und schreibt die Zeilen mit Änderungen in eine neue CSV-Datei.
    
    Args:
        file1 (str): Pfad zur ersten CSV-Datei.
        file2 (str): Pfad zur zweiten CSV-Datei.
        output_file (str): Pfad zur Ausgabedatei.
    """
    # Lese erste CSV-Datei ein und speichere Zeilen in einer Liste
    with open(file1, 'r') as file1_handle:
        csv_reader1 = csv.reader(file1_handle)
        file1_data = list(csv_reader1)
    
    # Lese zweite CSV-Datei ein und speichere Zeilen in einer Liste
    with open(file2, 'r') as file2_handle:
        csv_reader2 = csv.reader(file2_handle)
        file2_data = list(csv_reader2)
    
    # Vergleiche die Zeilen in beiden Dateien
    changes = []
    for row1, row2 in zip(file1_data, file2_data):
        if row1 != row2:
            changes.append(row2)
    
    # Schreibe die Zeilen mit Änderungen in eine neue CSV-Datei
    with open(output_file, 'w', newline='') as output_handle:
        csv_writer = csv.writer(output_handle)
        csv_writer.writerows(changes)
    
    print(f"Vergleich abgeschlossen! Änderungen wurden in {output_file} gespeichert.")