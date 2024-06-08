import nbformat

with open("lab11.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type == "code" and "execution_count" not in cell:
        cell["execution_count"] = None

with open("Krzysztof_Kołodziejyczk_lab11.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
