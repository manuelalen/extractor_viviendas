# Extractor de viviendas
**Descripción:** Software básico en Python para la extracción de las viviendas en régimen en alquiler en idealista

> [!CAUTION]
> Este repositorio está aún en construcción. El código mostrado al igual que cualquier otro documento aquí contenido, es temporal y sometido a grandes cambios.

> [!IMPORTANT]
> La versión definitiva del código en `Python` es una versión básica. Los conocimientos sobre este lenguaje son muy básicos por parte del autor y cualquier aportación adicional y más completa es bienvenida

## Proceso actual 🛳️

Aquí se podrá ir viendo la evolución del desarrollo del reporitorio al igual que su fase actual.

- [x] Inicio del repositorio 🏃‍♂️
- [x] Desarrollo de la versión inicial del software 💻
- [ ] Extracción de todos los datos de vivienda 🏠
- [ ] Creación del documento y la consulta vía API
- [ ] Mejora del software

## Cómo utilizar el software 🤓☝️

En esta sección se comenta cómo utilizar el software actual para poder lograr la extracción de los datos de vivienda utilizando el portal de [idealista](https://idealista.com).

La parte importante es el siguiente fragmento de código

```
if __name__ == "__main__":
    for page_num in range(2, 10):  # Cambie el rango para que vaya de la página 2 a la 60
        url = f"https://www.idealista.com/alquiler-viviendas/ourense-provincia/pagina-{page_num}.htm"
```
Aquí en la variable `url` tendremos que añadir la url de la provincia concreta que queramos extraer del portal idealista. Tener en cuenta que se realizará un bucle por el que se visitará desde la página 2 hasta el final de la misma. 

La página final se establece en el `for ... range`. En el ejemplo de código mostrado se observa que se visitará de la página 2 a la 10 dado que para **Ourense** hay un total de 10 páginas. El inicio siempre será la página 2 y la final el usuario tendrá que ir al portal idealista para esa provincia y observar cuántas paginas totales existen.

## Limitaciones ⚠️

La página inicial no podría obtenerse con este código dado que idealista, para cada provincia, la primera página no la muestra con el formato :

```
https://www.idealista.com/alquiler-viviendas/[PROVINCIA]-provincia/pagina-X.htm

```

Esto hace que no obtengamos todos los resultados, no obstante, para un análisis sobre el mercado de la vivienda, el muestreo suele ser suficiente si una provincia tuviese 4-5 páginas mínimo.
