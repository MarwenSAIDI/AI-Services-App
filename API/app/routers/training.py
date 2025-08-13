from fastapi import APIRouter

router = APIRouter(prefix="/train", tags=['Training'])

@router.post("/")
def start_training():
    train_id = "11-22-33"
    return {
        "result": f"Training {train_id} started"
    }