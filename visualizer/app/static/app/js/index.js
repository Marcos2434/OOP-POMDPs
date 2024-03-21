configs = {
    white: {
        canvas_bg: "rgb(255, 255, 255)",
        node_bg: "rgb(255, 255, 255)",
        node_border: "rgb(0, 0, 0)",
        node_highlight_bg: "rgb(255, 255, 255)",
        node_highlight_border: "rgb(0, 0, 0)",
        node_font_color: "rgb(0, 0, 0)",
        edge_color: "rgb(0, 0, 0)",
        nodeBorderSize: 2,
    },
    transparent: {
        canvas_bg: "rgb(47, 46, 51)",
        node_bg: "rgb(47, 46, 51)",
        node_border: "rgb(255, 255, 255)",
        node_highlight_bg: "rgb(47, 46, 51)",
        node_highlight_border: "rgb(255, 255, 255)",
        node_font_color: "rgb(255, 255, 255)",
        edge_color: "rgb(255, 255, 255)",
        nodeBorderSize: 2,
    },
}

config = configs.transparent;

class NetworkData {
    constructor(network, nodes, edges, target) {
        this.network = network
        this.nodes = nodes
        this.edges = edges
        this.target = target
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const mobileNav = document.querySelector(".hamburger");
    mobileNav.addEventListener("click", () => toggleNav());

    modelFormHandler()
    handleNetwrokContainerColor()
})

const handleNetwrokContainerColor = () => {
    const network_canvas = document.querySelector("#network");
    network_canvas.style.backgroundColor = config.canvas_bg;
}

const aspectRatio = () => {
    const network_canvas = document.querySelector("#network");
    const styles = getComputedStyle(network_canvas);
    network_canvas.style.height = styles.width;
    window.addEventListener("resize", () => network_canvas.style.height = styles.width);
}

const handleNetwork = ({model, target, size = 1, rows = 1, columns = 1}) => {

    const nodes = new vis.DataSet();
    const edges = new vis.DataSet();

    switch (model) {
        case "Line":
            
            // create the line model
            for (let i = 0; i < size; i++) {
                nodes.add({ id: i, label: i.toString() });
                if (i > 0) {
                    // if (i == target+1) {
                    //     edges.add({ from: i - 1, to: i, color: config.edge_color })
                    //     continue
                    // }
                    edges.add({ from: i - 1, to: i });
                }
            }

            break;
        case "Grid":
            // create the grid model
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    let id = i * size + j;
                    nodes.add({ id: id, label: id.toString() });
                    if (i > 0) {
                        edges.add({ from: id - size, to: id });
                    }
                    if (j > 0) {
                        edges.add({ from: id - 1, to: id });
                    }
                }
            }
            break;
        case "Maze":
            // create the maze model
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    let id = i * size + j;
                    nodes.add({ id: id, label: id.toString() });
                    if (i > 0) {
                        edges.add({ from: id - size, to: id });
                    }
                    if (j > 0) {
                        edges.add({ from: id - 1, to: id });
                    }
                }
            }
            break;
    }
    // // create an array with nodes
    // const nodes = new vis.DataSet([
    //     { id: 1, label: "1"},
    //     { id: 2, label: "2"},
    //     { id: 3, label: "3"},
    //     { id: 4, label: "4"},
    //     { id: 5, label: "5"},
    // ]);

    // // create an array with edges
    // const edges = new vis.DataSet([
    //     { from: 1, to: 3 },
    //     { from: 1, to: 2 },
    //     { from: 2, to: 4 },
    //     { from: 2, to: 5 },
    //     { from: 3, to: 3 },
    // ]);

    // create a network
    const container = document.getElementById("network")
    const data = { nodes, edges }
    const options = {
        autoResize: true,
        height: '100%',
        width: '100%',
        locale: 'en',
        clickToUse: false,
        configure: {},    // defined in the configure module.
        edges: {
            color: {
                color: config.edge_color,
                inherit: false, // Disable color inheritance
                opacity: 1.0
            }
        },        // defined in the edges module.
        nodes: {
            shape: "dot",
            size: 20,
            scaling: {
                label: {
                    min: 10,  // minimum font size
                    max: 30   // maximum font size
                }
            },
            font: {
                size: 20,
                face: 'Tahoma',
                color: config.node_font_color,
            }
        },        // defined in the nodes module.
        // groups: {},       // defined in the groups module.
        // layout: {},       // defined in the layout module.
        // manipulation: {}, // defined in the manipulation module.
        interaction: {
            dragView: false,
            zoomView: false,
        },  // defined in the interaction module.
        physics: {
            barnesHut: {
                springLength: 100, // Set your desired default edge length
                springConstant: 0.04 // Tweak other physics parameters if needed
            }
        },      // defined in the physics module.
    }
    const network = new vis.Network(container, data, options);
    
    nodeBorderSize = config.nodeBorderSize
    for (node of nodes.get()) {
        if (node.id == target) {
            node.color = {
                border: "green",  // Color of the border
                background: config.node_bg,  // Color of the background
                highlight: {  // Colors when the node is selected
                    border: "green",  // Color of the border
                    background: config.node_highlight_bg,  // Color of the background
                }
            }
            node.borderWidth = nodeBorderSize
            nodes.update(node)
            continue
        }
        node.color = {
            border: config.node_border,  // Color of the border
            background: config.node_bg,  // Color of the background
            highlight: {  // Colors when the node is selected
                border: config.node_highlight_border,  // Color of the border
                background: config.node_highlight_bg,  // Color of the background
            }
        }
        node.borderWidth = nodeBorderSize
        nodes.update(node)
    }

    // handle download button

    network.on("afterDrawing", ctx => {
        let dataURL = ctx.canvas.toDataURL();
        document.getElementById('downloadButton').onclick = () => {
          let link = document.createElement('a');
          link.download = 'network.png';
          link.href = dataURL;
          link.click();
        };
    });

    return new NetworkData(network, nodes, edges, target)
}

const handleNetworkSolution = ({networkData, solution}) => {
    const nodes = networkData.nodes

    colors = [
        "blue", "magenta", "lime", "olive", "purple", 
        "yellow", "pink", "orange", "red", "cyan", 
    ]
    availableColors = colors
    observableColors = {}

    // Give each observable a colour and update the nodes
    for (const [key, value] of Object.entries(solution)) {
        if (key.substring(0, 2) == 'ys') {

            // In state s, observable o is found, 1 yes, 0 no
            if (value == 1) {
                const s = parseInt(key[2]) // s for state
                const o = parseInt(key[3]) // o for observable
                
                // Check if the observable has already been mapped to a colour
                if (!observableColors[o]) observableColors[o] = availableColors.pop()

                for (node of nodes.get()) {
                    if (node.id == s) {
                        node.color = {
                            border: observableColors[o],
                            background: config.node_bg,
                            highlight: {
                                border: observableColors[o],
                                background: config.node_highlight_bg,
                            }
                        }
                        nodes.update(node)
                    }
                } 
            }
        }

    }

    const tableBodyRef = document.querySelector("#strat-table").querySelector("tbody")

    tableInfo = {}
    // Once each observable has been mapped to a colour, update the strategy table
    for (const [key, value] of Object.entries(solution)) {
        if (key.substring(0, 2) == 'xo') {
            const o = parseInt(key[2]) // o for observable
            const a = key[3] // a for action

            if (!tableInfo[o]) {
                tableInfo[o] = {
                    id: o,
                    color: observableColors[o],
                    actionProbabilities: {
                        right: 0,
                        left: 0,
                        up: 0,
                        down: 0,
                    }
                }
            }
            switch (a) {
                case 'l':
                    tableInfo[o].actionProbabilities.left = value
                    break
                case 'r':
                    tableInfo[o].actionProbabilities.right = value
                    break
                case 'u':
                    tableInfo[o].actionProbabilities.up = value
                    break
                case 'd':
                    tableInfo[o].actionProbabilities.down = value
                    break
            }
        }
    }
    
    // Clear table
    tableBodyRef.innerHTML = ""
    for (const [_, info] of Object.entries(tableInfo)) {
        const row = tableBodyRef.insertRow(-1)
        const cell1 = row.insertCell(0)
        const cell2 = row.insertCell(1)
        const cell3 = row.insertCell(2)
        const cell4 = row.insertCell(3)
        const cell5 = row.insertCell(4)

        cell1.innerHTML = "hi!"
        cell1.innerHTML = "Strategy " + info.id + ": " + info.color
        
        for (const [action, prob] of Object.entries(info.actionProbabilities)) {
            switch (action) {
                case 'left':
                    cell3.innerHTML = prob
                    break
                case 'right':
                    cell2.innerHTML = prob
                    break
                case 'up':
                    cell4.innerHTML = prob
                    break
                case 'down':
                    cell5.innerHTML = prob
                    break
            }
        }
    }

    // // set the edge of the node next to the target node to the next node's color
    // for (node of nodes.get()) {
    //     if (node.id == networkData.target+1) {
    //         networkData.edges.update({ from: node.id - 1, to: node.id, color: node.color.border })
    //         break
    //     }
    // }

    return networkData
}

const toggleNav = () => {
    const navbar = document.querySelector(".menubar");
    const mobileNav = document.querySelector(".hamburger");
    navbar.classList.toggle("active");
    mobileNav.classList.toggle("hamburger-active");
};

const serializeForm = form => {
    // Serialize form data into JSON object
    const formData = new FormData(form)
    const data = {}
    for (const [key, value] of formData.entries()) {
        data[key] = value
    }
    return data
}

const modelFormHandler = () => {
    form = document.querySelector('#oop_form')
    let form_data = serializeForm(form)
    let networkData = handleNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})

    form.addEventListener('submit', async event => {
        event.preventDefault()
        
        const loader = document.querySelector("#loader")
        loader.classList.remove("disappear")

        const counter = document.querySelector("#counter")
        counter.innerHTML = 0
        const increaseCounter = () => counter.innerHTML = parseInt(counter.innerHTML) + 1
        const counterInterval = setInterval(increaseCounter, 1000)

        response = await fetch('api/createModel', {
            method: 'POST',
            body: JSON.stringify(serializeForm(form)),
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
        })

        clearInterval(counterInterval)
        loader.classList.add("disappear")

        if (response.status === 200) {
            const data = await response.json()

            if (data.solution == "No solution") {
                alert("No solution found for the given model")
                return
            } else if (data.solution == "Unknown") {
                alert("Unknown error")
                return
            }

            networkData = handleNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
            networkData = handleNetworkSolution({networkData, solution: data.solution})
        } else {
            console.error(response)
            alert("Error: " + response.status + "\n" + response.statusText)
        }
    })

    
    form.addEventListener('change', event => {
        form_data = serializeForm(form)
        networkData = handleNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
    })

    document.querySelector("#theme-select").addEventListener("change", e => {
        config = configs[e.target.value];
        networkData = handleNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
        handleNetwrokContainerColor();
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// const csrftoken = getCookie('csrftoken');