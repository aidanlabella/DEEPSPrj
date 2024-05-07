CREATE TABLE agg AS
    SELECT 
        aer.lon,
        aer.lat,
        aer.lev,
        aer.time,
        aer.AIRDENS,
        aer.SO4,
        aer.SO2,
        aer.RH,
        aer.PS,
        asm.H,
        asm.O3,
        asm.T,
        asm.U,
        asm.V,
        chm.CO
        FROM aer_nv AS aer
        JOIN asm_nv AS asm ON aer.lon = asm.lon AND aer.lat = asm.lat AND aer.time = asm.time
        JOIN chm_nv AS chm ON asm.lon = chm.lon AND asm.lat = chm.lat AND asm.time = chm.time
        WHERE aer.lon = 41.875 -- This is the longitude of Southern New England (roughly)
        ORDER BY RANDOM()
        LIMIT 1000000; 
