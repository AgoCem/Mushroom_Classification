from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionManipulationConfig:
    root_dir: Path
    local_data_file: Path
    source_URL: str
    save_training_file: Path
    param_target_col: str
    param_random_state: int


@dataclass(frozen=True)
class ModelPreparationTrainingConfig:
    root_dir: Path
    save_models: Path
    param_target_col: str
    param_random_state: int
    param_n_estimators: list
    param_c_svc: list
    param_gamma_svc: list
    param_c_log_reg: list
    param_number_cv: int