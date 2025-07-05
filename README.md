esesesesesttyt

def graficar_libros_por_nacionalidad():
    nacionalidades = [libro.autor.nacionalidad for libro in Libro.objects.all()]
    conteo = Counter(nacionalidades)

    plt.figure()
    plt.pie(conteo.values(), labels=conteo.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Libros por Nacionalidad del Autor')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
  
    graficar_promedio_calificacion_por_autor()
    graficar_distribucion_calificaciones()
    graficar_libros_por_nacionalidad()
