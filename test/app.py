import streamlit as st
import numpy as np

def main():
    # Título de la aplicación
    st.title("Cálculo de Componentes de Tensión")

    # Introducción de los componentes del tensor de tensiones
    st.header("Introduce el tensor de tensiones")

    # Crear campos de entrada para la parte triangular superior de la matriz 3x3
    matrix_input = np.zeros((3, 3))
    for i in range(3):
        for j in range(i, 3):
            value = st.number_input(f'Elemento ({i+1}, {j+1})', key=f'{i}{j}')
            matrix_input[i, j] = value
            if i != j:
                matrix_input[j, i] = value  # Rellenar la parte simétrica


    # Mostrar la matriz completa en pantalla
    st.subheader('Matriz del Tensor:')
    st.write(matrix_input)


    # Introducción del vector normal del plano
    st.header("Introduce el vector normal del plano, debe de ser unitario o se normalizará automáticamente")
    n_x = st.number_input("n_x", value=1.0)
    n_y = st.number_input("n_y", value=0.0)
    n_z = st.number_input("n_z", value=0.0)


    # Construir el vector normal y normalizarlo
    n = np.array([n_x, n_y, n_z])
    n_norm = np.linalg.norm(n)

    if n_norm == 0:
        st.error("El vector normal no puede ser el vector nulo.")
    else:
        if not np.isclose(n_norm, 1.0):
            st.warning("El vector normal no es unitario. Se normalizará automáticamente.")
            n = n / n_norm

        
    if (st.button("Calcular tension")):

        # Calcular la tensión en la dirección del plano
        T = np.dot(matrix_input, n)
        # Mostrar los resultados
        st.subheader("Componentes de la tensión en la dirección del plano")
        st.write(f"σ_x = {T[0]:.2f}")
        st.write(f"σ_y = {T[1]:.2f}")
        st.write(f"σ_z = {T[2]:.2f}")
  
    if (st.button("Calcular componentes intrinsecas")):

        # Calcular la tensión en la dirección del plano
        T = np.dot(matrix_input, n)
        # Mostrar los resultados
        st.subheader("Componentes de la tensión en la dirección del plano")
        st.write(f"σ_n = {T[0]:.2f}")
        st.write(f"τ_n = {T[1]:.2f}")




main()