-- Comparación de Precios entre Supermercados: Determinar qué supermercados ofrecen los precios más bajos y cuáles son más caros para cada producto.
SELECT min(precio) AS precio_minimo, max(precio) AS precio_maximo, s.supermercado , c.categoria 
FROM datos_historicos dh 
inner JOIN supermercado s 
ON dh.id_supermercado = s.id_supermercado 
INNER JOIN categoria c 
ON dh.id_categoria = c.id_categoria 
WHERE dh.fecha = '26-10-2024'
GROUP BY c.categoria, s.supermercado 
ORDER BY c.categoria, s.supermercado;

-- Análisis de la Evolución de Precios: Estudiar cómo han cambiado los precios de los productos a lo largo del tiempo en distintos supermercados.

SELECT dh.fecha, s.supermercado , c.categoria , sum(dh.variación) 
OVER (PARTITION BY s.supermercado, c.categoria ORDER BY dh.fecha) AS Variacion_acumulada
FROM datos_historicos dh 
INNER JOIN supermercado s ON dh.id_supermercado = s.id_supermercado 
INNER JOIN categoria c ON dh.id_categoria = c.id_categoria 
ORDER BY c.categoria, s.supermercado, dh.fecha;

-- Detección de Anomalías: Identificar subidas o bajadas de precios inusuales que podrían señalar prácticas abusivas o promociones.

SELECT fecha, s.supermercado , c.categoria , sum(dh.variación) AS picos_precios
FROM datos_historicos dh 
INNER JOIN supermercado s ON dh.id_supermercado = s.id_supermercado 
INNER JOIN categoria c ON dh.id_categoria = c.id_categoria 
GROUP BY c.categoria , s.supermercado , dh.fecha;

-- Análisis de la Dispersión de Precios: Evaluar la variabilidad de los precios de un mismo producto en diferentes supermercados.
SELECT c.categoria , s.supermercado, 
		avg(dh.precio) AS precio_promedio,
		min(dh.precio) AS precio_minimo,
		max(dh.precio) AS precio_maximo
FROM datos_historicos dh 
inner JOIN supermercado s 
ON dh.id_supermercado = s.id_supermercado 
INNER JOIN categoria c 
ON dh.id_categoria = c.id_categoria 
GROUP BY c.categoria, s.supermercado 
ORDER BY c.categoria;

-- Comparación de Precios Promedio: Calcular y comparar los precios promedio de cada producto en diferentes supermercados.

SELECT round(CAST (avg(precio) AS NUMERIC), 2) AS precio_pomedio, s.supermercado , c.categoria 
FROM datos_historicos dh 
inner JOIN supermercado s 
ON dh.id_supermercado = s.id_supermercado 
INNER JOIN categoria c 
ON dh.id_categoria = c.id_categoria 
GROUP BY s.supermercado , c.categoria 
ORDER BY c.categoria;