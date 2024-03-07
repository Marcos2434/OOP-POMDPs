document.addEventListener("DOMContentLoaded", () => {
    console.log("Hello World");

    const mobileNav = document.querySelector(".hamburger");
    mobileNav.addEventListener("click", () => toggleNav());

    handleNetwork();
    // handleNetwrokContainer();
})

const handleNetwrokContainer = () => {
    const network_canvas = document.querySelector("#network");
    const styles = getComputedStyle(network_canvas);
    network_canvas.style.height = styles.width;
    window.addEventListener("resize", () => network_canvas.style.height = styles.width);
}

const handleNetwork = () => {
    // create an array with nodes
    var nodes = new vis.DataSet([
        { id: 1, label: "Node 1" },
        { id: 2, label: "Node 2" },
        { id: 3, label: "Node 3" },
        { id: 4, label: "Node 4" },
        { id: 5, label: "Node 5" },
    ]);

    // create an array with edges
    var edges = new vis.DataSet([
        { from: 1, to: 3 },
        { from: 1, to: 2 },
        { from: 2, to: 4 },
        { from: 2, to: 5 },
        { from: 3, to: 3 },
    ]);

    // create a network
    var container = document.getElementById("network");
    var data = {
        nodes: nodes,
        edges: edges,
    };
    var options = {};
    var network = new vis.Network(container, data, options);
}

const toggleNav = () => {
    const navbar = document.querySelector(".menubar");
    const mobileNav = document.querySelector(".hamburger");
    navbar.classList.toggle("active");
    mobileNav.classList.toggle("hamburger-active");
};

