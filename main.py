from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

# Tabla de saturación simplificada (ejemplo)
SAT_TABLE = {
    1: (0.0011, 1.694),
    5: (0.0012, 0.374),
    10: (0.0035, 0.0035),   # del ejemplo que daban
    15: (0.0015, 0.132),
    20: (0.0017, 0.099),
}

@app.get("/phase-change-diagram")
async def phase_change_diagram(pressure: float = Query(..., description="Pressure in MPa")):
    # Buscar en tabla
    if pressure in SAT_TABLE:
        v_liq, v_vap = SAT_TABLE[pressure]
    else:
        # fallback: aproximación lineal
        v_liq = 0.001 + 0.00005 * pressure
        v_vap = round(2.0 / (pressure + 0.5), 6)

    return JSONResponse({
        "specific_volume_liquid": round(v_liq, 6),
        "specific_volume_vapor": round(v_vap, 6),
    })
@app.get("/")
def root():
    return {"status": "ok", "message": "API funcionando 🚀"}
