from fastapi import APIRouter, HTTPException
from schemas import PaymentCreate, PaymentResponse
import database
from datetime import datetime

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=PaymentResponse)
async def create_payment(payment: PaymentCreate):
    if database.pg_pool is None:
        raise HTTPException(status_code=503, detail="Database not initialized")

    async with database.pg_pool.acquire() as conn:
        row = await conn.fetchrow("""
            INSERT INTO payments (user_id, amount, status)
            VALUES ($1, $2, $3)
            RETURNING id, user_id, amount, status, created_at
        """, payment.user_id, payment.amount, payment.status)
    return dict(row)

@router.get("/{payment_id}", response_model=PaymentResponse)
async def get_payment(payment_id: int):
    if database.pg_pool is None:
        raise HTTPException(status_code=503, detail="Database not initialized")

    async with database.pg_pool.acquire() as conn:
        row = await conn.fetchrow("""
            SELECT id, user_id, amount, status, created_at
            FROM payments WHERE id = $1
        """, payment_id)

    if not row:
        raise HTTPException(status_code=404, detail="Payment not found")

    return dict(row)

@router.get("/", response_model=list[PaymentResponse])
async def list_payments(limit: int = 10):
    if database.pg_pool is None:
        raise HTTPException(status_code=503, detail="Database not initialized")

    async with database.pg_pool.acquire() as conn:
        rows = await conn.fetch("""
            SELECT id, user_id, amount, status, created_at
            FROM payments
            ORDER BY created_at DESC
            LIMIT $1
        """, limit)

    return [dict(row) for row in rows]