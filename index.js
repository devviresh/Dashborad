const sidemenu = document.querySelector("aside");
const menubtn = document.querySelector("#menu-btn");
const closebtn = document.querySelector("#close-btn");
const themetoggler = document.querySelector(".theme-toggler");

//show sidebar
menubtn.addEventListener("click", () => {
    sidemenu.style.display="block";
})

//close sidebar
closebtn.addEventListener("click", () => {
    sidemenu.style.display="none";
})

//change theme
themetoggler.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme-variables");
    themetoggler.querySelector("span:nth-child(1)").classList.toggle("active");
    themetoggler.querySelector("span:nth-child(2)").classList.toggle("active");
})

// Fill orders in table
Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
                    <td>${order.productName}</td>
                    <td>${order.productNumber}</td>
                    <td>${order.paymentStatus}</td>
                    <td class="${order.shipping === "Declined" ? "danger" : order.shipping === "Pending" ? "warning" : "primary"}">${order.shipping}</td>
                    <td class="primary">Details</td>                    
                    `;
    tr.innerHTML = trContent;
    document.querySelector("table tbody").appendChild(tr);
})