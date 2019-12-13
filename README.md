# Redes neuronales aplicadas al reconocimiento básico de lenguaje de señas en fotografías

Publicado el 13 de diciembre del 2019.

## Motivación
Proyecto para el curso Inteligencia Artificial, de la carrera Ciencias de la Computación e Informática de la **Universidad de Costa Rica**.

## Descripción del proyecto
Inferencia el motivo de una seña en LESCO (Lenguaje de Señas Costarricese) mediante el análisis de sentimientos en el rostro de la persona que realiza dicha. Esto mediante OpenCv para la obtención de los rostros de imagenes con más contenido y redes neuronales para la clasificación de los gestos y de las emociones en los rostros. Se utiliza agrupamiento (clustering) con k-means en las imágenes, aplicadas al color.

## Tecnologías
Redes neuronales, OpenCV, Tensorflow, Python 3

## Trabajo realizado
Actualmente el trabajo cuenta con la detección de rostros en imágenes grandes, que contienen muchos otros elementos, lo que generará las entradas para la red que reconoce las emociones en rostros. Se crearon dos redes neuronales como se describe en este documento, que por el momento funcionan con datos genéricos, pero que son capaces de funcionar con datos reales. 
        
Para que el proyecto se de por completado, es necesario unir todas sus partes, de manera que se pueda pasar una imagen completa de un individuo realizando una seña y que se pueda dar el resultado esperado: generar una aproximación a lo que el individuo quiso expresar al realizar dicha seña, esto al analizar el sentimiento expresado en su cara.
        
Se desea agregar nuevas emociones para que el análisis sea más específico y pueda generar más valor.
        
Se espera que en un futuro se inviertan recursos económicos y de tiempo en la generación de un conjunto de datos lo suficientemente grande de señas en LESCO que permita realizar trabajos similares al aquí descrito.

## Replicación del rabajo realizado
En el directorio *resources*, se encuentran los archivos donde se describe primero la estructura de directorios deseada para correr exitosamente el proyecto y uno con los enlaces para descargar los conjuntos de datos utilizados para nuestra investigación. Esto no restringe de ningún modo la utilización de otros datos.

## Agradecimientos
Dr.rer.nat. Alvaro de la Osa, profesor que dirigió la investigación. 
