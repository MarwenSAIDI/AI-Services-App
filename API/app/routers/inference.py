from fastapi import APIRouter

router = APIRouter(prefix="/inference", tags=["Inference"])

@router.post("/")
def predict_label():
    return {
        "result": "Label Predicted Successfully"
    }

@router.get("/{item_id}")
def get_label(item_id: str):
    return {
        "result": f"Label of {item_id} is 0"
    }