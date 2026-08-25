# techlabs_trees_26

Deep learning pipeline for **tree species detection** in aerial orthophotos of Münster city centre, built with Faster R-CNN (ResNet-50 FPN backbone). Developed as part of the TechLabs Münster Deep Learning track, Summer Semester 2026, Group 2.

---

## Project Overview

The goal of this project is to automatically detect and classify tree species from high-resolution aerial imagery (`.jp2` tiles, 10 cm ground resolution). A Faster R-CNN object detection model is trained on a labelled street-tree dataset and evaluated using standard COCO metrics (mAP).

### Key steps in the pipeline

1. **Data loading** – Load multi-band orthophoto tiles (`.jp2`) and the tree cadastre (GeoJSON / GeoPackage).
2. **CRS unification** – Reproject tree coordinates to match the raster CRS.
3. **Geo-to-pixel conversion** – Map tree geo-coordinates to pixel positions within each tile.
4. **Tree selection** – Filter trees that fall inside a given tile.
5. **Box creation** – Generate fixed-size bounding boxes (default 160 px) around each tree centroid.
6. **Patch extraction** – Cut large tiles (10 000 × 10 000 px) into 1 024 × 1 024 px patches.
7. **Dataset & DataLoader** – `TreePatchDataset` (PyTorch) with train / val / test split (70 / 15 / 15).
8. **Model** – Faster R-CNN with a custom classification head for the detected number of tree species; rare species are grouped into a *"Sonstige"* (other) class.
9. **Training** – Standard SGD training loop with configurable epochs, learning rate, and batch size.
10. **Evaluation** – Loss curves, mAP on test set (via `torchmetrics`), and visual inspection.

---

## Repository Structure

```
techlabs_trees_26/
├── DL_Gr2_2026SoSe_abgabe.ipynb   # Main notebook (full pipeline, designed for Google Colab)
├── github_temp.ipynb               # Scratch / experimental notebook
├── howto_and_best_practice.md      # Git workflow guide for the team
├── README.md
├── DATA_HIDDEN_FOR_GIT/            # Data folder (not tracked by Git)
│   ├── *.jp2                       # Orthophoto tiles (NRW open data, EPSG:25832)
│   ├── gruen_opendata.geojson      # Raw tree cadastre (open data)
│   ├── baeume.gpkg                 # Filtered / validated tree cadastre
│   └── more_tiles/                 # Additional orthophoto tiles
├── meeting_notes/                  # Project management notes
├── results/
│   └── test_metrics.json           # Saved evaluation metrics (mAP, mAR, …)
└── src/                            # Reusable Python modules
    ├── load_data.py                # load_tile_local(), load_trees_local()
    ├── convert_crs.py              # unify_crs(), trees_geo_to_pixel()
    ├── tree_selection.py           # tree_selection(), remove_non_trees()
    └── box_creation.py             # create_boxes(), plot_boxes_on_tile()
```

---

## Data

The project uses open geodata from the state of North Rhine-Westphalia (NRW):

- **Orthophotos** – DOP10 RGBI tiles (10 cm resolution, EPSG:25832), tiles `404_5757`, `404_5758`, `405_5757`, `405_5758`, and additional tiles in `more_tiles/`.
- **Tree cadastre** – `gruen_opendata.geojson` (raw) and `baeume.gpkg` (expert-validated subset).

Data files are stored in `DATA_HIDDEN_FOR_GIT/` which is excluded from version control. Download or place the files there before running the notebook.

---

## Setup & Usage

The main notebook is designed to run on **Google Colab** with the project folder mounted from Google Drive.

### 1. Mount Google Drive (Colab)

```python
from google.colab import drive
drive.mount('/content/drive')
```

### 2. Set the project root path

In the configuration cell, update `PROJECT_ROOT_DIR` to point to the location of this repository on your Drive:

```python
PROJECT_ROOT_DIR = '/content/drive/MyDrive/techlabs_trees_26'
```

### 3. Place data

Copy the contents of `DATA_HIDDEN_FOR_GIT/` into a `DATA/` folder inside the project root on Drive.

### 4. Run the notebook

Execute `DL_Gr2_2026SoSe_abgabe.ipynb` top to bottom.

---

## Key Configuration Parameters

| Parameter | Default | Description |
|---|---|---|
| `NTILES` | `4` | Number of orthophoto tiles to load |
| `BOX_WIDTH` | `160` px | Side length of bounding boxes around tree centroids |
| `PATCH_SIZE` | `1024` px | Size of image patches fed to the model |
| `PATCH_STRIDE` | `1024` px | Stride for patch extraction (no overlap) |
| `RARE_SPECIES_THRESHOLD` | `100` | Min. instances to keep a species; rarer ones → *"Sonstige"* |
| `TRAIN_FRAC` / `VAL_FRAC` | `0.70` / `0.15` | Train / validation split fractions |
| `NUM_EPOCHS` | `5` | Training epochs |
| `LEARNING_RATE` | `0.005` | SGD learning rate |
| `BATCH_SIZE` | `2` | Batch size |

---

## Results

Current test-set metrics (see `results/test_metrics.json`):

| Metric | Value |
|---|---|
| mAP (IoU 0.50:0.95) | 0.011 |
| mAP@50 | 0.023 |
| mAP@75 | 0.008 |
| mAR@100 | 0.073 |

These are early-stage results with a small number of training epochs and a limited number of tiles — further tuning is expected to improve performance.

---

## Dependencies

- Python ≥ 3.9
- `torch`, `torchvision`
- `torchmetrics`
- `rasterio`
- `geopandas`
- `numpy`, `matplotlib`

---

## Team

TechLabs Münster · Deep Learning Track · Summer Semester 2026 · Group 2