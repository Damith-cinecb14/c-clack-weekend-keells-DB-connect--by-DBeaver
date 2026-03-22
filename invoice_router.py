from fastapi import APIRouter
from starlette.exceptions import HTTPException

from models import InvoiceCreate
import invoice_repository as repo

router = APIRouter(prefix="/invoice", tags=["invoice"])

@router.post("/")
def create_invoice(invoice:InvoiceCreate):
    result = repo.create_invoice(invoice.user_id,invoice.amopunt,invoice.description)
    return {
        "id" : result[0],
        "user_id" : result[1],
        "amount": result[2],
        "description": result[3]
    }


@router.get("/{invoice_id}")
def get_invoice(invoice_id:int):
    result = repo.get_invoice(invoice_id)
    if not  result:
        raise HTTPException(status_code=404, detail="invoice not found")

    return {
        "id": result[0],
        "user_id": result[1],
        "amount": result[2],
        "description": result[3]
            }

@router.get("")
def get_invoices():
    invoices =repo.get_invoices()
    invoice_list = []

    for invoice in invoices:
        invoice_list.append(
            { "id": invoice[0],
        "user_id": invoice[1],
        "amount": invoice[2],
        "description": invoice[3]
             }
        )
    return invoice_list

@router.delete("/invoice_id")
def delete_invoice(invoice_id:int):
    repo.delete_invoice(invoice_id)
    return {"response" :"Invoice Deleted Successfully"}