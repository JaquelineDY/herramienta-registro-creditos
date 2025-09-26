let grafica;
const API_URL = "/creditos";

function actualizarGrafica(total) {
  const ctx = document.getElementById("graficaCanvas").getContext("2d");

  if (grafica) grafica.destroy();

  grafica = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Total Créditos"],
      datasets: [
        {
          label: "Monto total",
          data: [total],
          backgroundColor: "rgba(54, 162, 235, 0.7)",
        },
      ],
    },
  });
}

function actualizarGraficaDistribucion(creditos) {
  const ctx = document.getElementById("graficaCanvas").getContext("2d");

  if (grafica) grafica.destroy();

  // Agrupar créditos por cliente
  const distribucionClientes = creditos.reduce((acc, credito) => {
    acc[credito.cliente] = (acc[credito.cliente] || 0) + credito.monto;
    return acc;
  }, {});

  // Preparación de datos para la gráfica
  const labels = Object.keys(distribucionClientes);
  const data = Object.values(distribucionClientes);

  grafica = new Chart(ctx, {
    type: "pie",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Distribución por Cliente",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132, 0.7)",
            "rgba(54, 162, 235, 0.7)",
            "rgba(255, 206, 86, 0.7)",
            "rgba(75, 192, 192, 0.7)",
            "rgba(153, 102, 255, 0.7)",
            "rgba(255, 159, 64, 0.7)",
          ],
        },
      ],
    },
  });
}

function listarCreditos() {
  fetch(`${API_URL}`)
    .then((response) => response.json())
    .then((creditos) => {
      const tabla = document.getElementById("tabla-creditos");
      tabla.innerHTML = "";
      creditos.forEach((c) => {
        const fila = `
          <tr>
            <td>${c.id}</td>
            <td>${c.cliente}</td>
            <td>${c.monto}</td>
            <td>${c.tasa_interes}%</td>
            <td>${c.plazo}</td>
            <td>${c.fecha_otorgamiento}</td>
            <td>
              <button onclick="editarCredito(${c.id}, '${c.cliente}', ${c.monto}, ${c.tasa_interes}, ${c.plazo}, '${c.fecha_otorgamiento}')">Editar</button>
              <button onclick="eliminarCredito(${c.id})">Eliminar</button>
            </td>
          </tr>
        `;
        tabla.innerHTML += fila;
      });
    });
}

async function editarCredito(id, cliente, monto, tasa, plazo, fecha) {
  const nuevoCliente = prompt("Cliente:", cliente);
  if (!nuevoCliente) return;

  const nuevoMonto = parseFloat(prompt("Monto:", monto));
  const nuevaTasa = parseFloat(prompt("Tasa de interés:", tasa));
  const nuevoPlazo = parseInt(prompt("Plazo (meses):", plazo));
  const nuevaFecha = prompt("Fecha (YYYY-MM-DD):", fecha);

  const data = {
    cliente: nuevoCliente,
    monto: nuevoMonto,
    tasa_interes: nuevaTasa,
    plazo: nuevoPlazo,
    fecha_otorgamiento: nuevaFecha,
  };

  await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  listarCreditos();
}

// Funcionalidad para la barra lateral dinámica
const hamburger = document.getElementById("hamburger");
const sidebar = document.getElementById("sidebar");

// Alternar la barra lateral al hacer clic en el botón de hamburguesa
hamburger.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});

// Cerrar la barra lateral al hacer clic fuera de ella
document.addEventListener("click", (event) => {
  if (!sidebar.contains(event.target) && !hamburger.contains(event.target)) {
    sidebar.classList.remove("active");
  }
});

// Función para mostrar el popup con un mensaje específico
function mostrarPopup(mensaje) {
  const popup = document.getElementById("popup");
  const popupMessage = document.getElementById("popup-message");

  popupMessage.textContent = mensaje; // Establecer el mensaje
  popup.classList.remove("hidden");
  popup.classList.add("visible");

  // Ocultar el popup automáticamente después de 3 segundos
  setTimeout(() => {
    popup.classList.remove("visible");
    popup.classList.add("hidden");
  }, 3000);
}

// Mostrar el popup al cargar la página
document.addEventListener("DOMContentLoaded", () => {
  mostrarPopup("¡Bienvenido al sistema de gestión de créditos!");
  fetch(API_URL)
    .then((response) => response.json())
    .then((creditos) => {
      const totalMonto = creditos.reduce((sum, credito) => sum + credito.monto, 0);
      actualizarGrafica(totalMonto); // Actualizar la gráfica con el monto total
      actualizarGraficaDistribucion(creditos); // Mostrar distribución por cliente
    })
    .catch((error) => console.error("Error al obtener los créditos para la gráfica:", error));
});
