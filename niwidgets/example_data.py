"""Example files for use with niwidgets."""
__all__ = [
    "example_atlas",
    "example_zmap",
    "example_t1",
    "example_surface",
    "example_overlay",
    "streamlines",
]

from pathlib import Path

root_dir = Path(__file__).resolve() / "data"

example_atlas = root_dir / "cc400_roi_atlas.nii"
example_zmap = root_dir / "cognitive control_pFgA_z.nii.gz"
example_t1 = root_dir / "T1.nii.gz"

surface_dir = root_dir / "example_surfaces"

example_surface = surface_dir / "lh.inflated"

example_overlay = {
    key: surface_dir / f
    for key, f in zip(
        ["Area", "Curvature", "Thickness", "Annotation"],
        ("lh.area", "lh.curv", "lh.thickness", "lh.aparc.annot"),
    )
}

streamlines = root_dir / "streamlines.trk"
