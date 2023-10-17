import datetime

class HojaAnestesia:
    def __init__(self):
        self.paciente_nombre = ""
        self.edad = ""
        self.peso = ""
        self.procedimiento = ""
        self.fecha = ""
        self.hora = ""
        self.anestesiologo = ""
        self.medicamentos = []
        self.signos_vitales = {}

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def agregar_signos_vitales(self, tiempo, presion_arterial, frecuencia_cardiaca, saturacion_oxigeno):
        self.signos_vitales[tiempo] = {
            "Presión Arterial": presion_arterial,
            "Frecuencia Cardiaca": frecuencia_cardiaca,
            "Saturación de Oxígeno": saturacion_oxigeno
        }

    def mostrar_datos(self):
        print("Hoja de Anestesia")
        print("Paciente: ", self.paciente_nombre)
        print("Edad: ", self.edad)
        print("Peso: ", self.peso)
        print("Procedimiento: ", self.procedimiento)
        print("Fecha: ", self.fecha)
        print("Hora: ", self.hora)
        print("Anestesiólogo: ", self.anestesiologo)
        print("Medicamentos administrados:")
        for medicamento in self.medicamentos:
            print("  -", medicamento)
        print("Signos Vitales:")
        for tiempo, signos in self.signos_vitales.items():
            print(f"Tiempo: {tiempo}")
            for clave, valor in signos.items():
                print(f"  - {clave}: {valor}")

def main():
    hoja = HojaAnestesia()

    hoja.paciente_nombre = input("Nombre del paciente: ")
    hoja.edad = input("Edad del paciente: ")
    hoja.peso = input("Peso del paciente: ")
    hoja.procedimiento = input("Procedimiento: ")
    hoja.fecha = datetime.date.today().strftime("%Y-%m-%d")
    hoja.hora = datetime.datetime.now().strftime("%H:%M:%S")
    hoja.anestesiologo = input("Nombre del anestesiólogo: ")

    while True:
        medicamento = input("Ingrese un medicamento administrado (o escriba 'fin' para salir): ")
        if medicamento.lower() == "fin":
            break
        hoja.agregar_medicamento(medicamento)

    print("Ingrese los signos vitales cada 5 minutos. Para detener, escriba 'fin' cuando se le pida el tiempo.")
    
    tiempo = 0
    while True:
        tiempo_str = input(f"Ingrese el tiempo ({tiempo} minutos): ")
        if tiempo_str.lower() == "fin":
            break
        
        presion_arterial = input("Presión Arterial: ")
        frecuencia_cardiaca = input("Frecuencia Cardiaca: ")
        saturacion_oxigeno = input("Saturación de Oxígeno: ")

        hoja.agregar_signos_vitales(f"{tiempo} minutos", presion_arterial, frecuencia_cardiaca, saturacion_oxigeno)
        tiempo += 5

    hoja.mostrar_datos()
    
    nombre_archivo = input("Ingrese el nombre del archivo para guardar los datos: ")
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Hoja de Anestesia\n")
        archivo.write("Paciente: " + hoja.paciente_nombre + "\n")
        archivo.write("Edad: " + hoja.edad + "\n")
        archivo.write("Peso: " + hoja.peso + "\n")
        archivo.write("Procedimiento: " + hoja.procedimiento + "\n")
        archivo.write("Fecha: " + hoja.fecha + "\n")
        archivo.write("Hora: " + hoja.hora + "\n")
        archivo.write("Anestesiólogo: " + hoja.anestesiologo + "\n")
        archivo.write("Medicamentos administrados:\n")
        for medicamento in hoja.medicamentos:
            archivo.write("  - " + medicamento + "\n")
        archivo.write("Signos Vitales:\n")
        for tiempo, signos in hoja.signos_vitales.items():
            archivo.write("Tiempo: " + tiempo + "\n")
            for clave, valor in signos.items():
                archivo.write("  - " + clave + ": " + valor + "\n")
    print(f"Datos guardados en '{nombre_archivo}'.")

if __name__ == "__main__":
    main()
