import gradio as gr

def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido a Gradio en Azure."

def suma(a, b):
    return float(a) + float(b)

with gr.Blocks() as demo:
    gr.Markdown("# Demo de Gradio en Azure")
    
    with gr.Tab("Saludo"):
        nombre_input = gr.Textbox(label="Tu nombre")
        saludo_output = gr.Textbox(label="Saludo")
        saludar_btn = gr.Button("Saludar")
    
    with gr.Tab("Calculadora"):
        with gr.Row():
            num1 = gr.Number(label="Primer número")
            num2 = gr.Number(label="Segundo número")
        suma_btn = gr.Button("Sumar")
        resultado = gr.Number(label="Resultado")
    
    saludar_btn.click(fn=saludar, inputs=nombre_input, outputs=saludo_output)
    suma_btn.click(fn=suma, inputs=[num1, num2], outputs=resultado)

if __name__ == "__main__":
    demo.launch()
