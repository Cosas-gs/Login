//Conectamos con el archivo y creamos el evento
document.getElementById("ticketForm").addEventListener("submit", function(event) {
    event.preventDefault();
  //Creamos las variables de los datos a almacenar
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;
  
    var ticket = {
      name: name,
      email: email,
      subject: subject,
      message: message
    };
  
    // Aquí puedes enviar el ticket a través de una solicitud HTTP o realizar alguna otra acción
    
    addTicketToList(ticket);
    clearForm();
  });
  //Creamos la funcion para visualizar los tickes anteriores en pantalla
  function addTicketToList(ticket) {
    var ticketList = document.getElementById("ticketList");
    var ticketDiv = document.createElement("div");
    ticketDiv.classList.add("ticket");
  
    var ticketHTML = `
      <h3>${ticket.subject}</h3>
      <p>Nombre: ${ticket.name}</p>
      <p>Email: ${ticket.email}</p>
      <p>Mensaje: ${ticket.message}</p>
    `;
  
    ticketDiv.innerHTML = ticketHTML;
    ticketList.appendChild(ticketDiv);
  }
  //Al almacenar los datos tambien quitamos los que se cargaron en el formulario anteriormente
  function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("subject").value = "";
    document.getElementById("message").value = "";
  }