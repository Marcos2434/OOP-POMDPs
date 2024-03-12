configs = {
    white: {
        canvas_bg: "rgb(255, 255, 255)",
        node_bg: "rgb(255, 255, 255)",
        node_border: "rgb(0, 0, 0)",
        node_highlight_bg: "rgb(255, 255, 255)",
        node_highlight_border: "rgb(0, 0, 0)",
        node_font_color: "rgb(0, 0, 0)",
    },
    transparent: {
        canvas_bg: "rgb(47, 46, 51)",
        node_bg: "rgb(47, 46, 51)",
        node_border: "rgb(255, 255, 255)",
        node_highlight_bg: "rgb(47, 46, 51)",
        node_highlight_border: "rgb(255, 255, 255)",
        node_font_color: "rgb(255, 255, 255)",
    }
}

config = configs.transparent;

document.addEventListener("DOMContentLoaded", () => {
    const mobileNav = document.querySelector(".hamburger");
    mobileNav.addEventListener("click", () => toggleNav());

    modelFormHandler()
    handleNetwork()
    handleNetwrokContainerColor()
    
    document.querySelector("#theme-select").addEventListener("change", e => {
        config = configs[e.target.value];
        handleNetwork();
        handleNetwrokContainerColor();
    });
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

const handleNetwork = () => {
    // create an array with nodes
    const nodes = new vis.DataSet([
        { id: 1, label: "1"},
        { id: 2, label: "2"},
        { id: 3, label: "3"},
        { id: 4, label: "4"},
        { id: 5, label: "5"},
    ]);

    // create an array with edges
    const edges = new vis.DataSet([
        { from: 1, to: 3 },
        { from: 1, to: 2 },
        { from: 2, to: 4 },
        { from: 2, to: 5 },
        { from: 3, to: 3 },
    ]);

    // create a network
    const container = document.getElementById("network");
    const data = {
        nodes: nodes,
        edges: edges,
    };
    const options = {
        autoResize: true,
        height: '100%',
        width: '100%',
        locale: 'en',
        clickToUse: false,
        configure: {},    // defined in the configure module.
        edges: {},        // defined in the edges module.
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
        physics: {},      // defined in the physics module.
    };

    const network = new vis.Network(container, data, options);
    
    for (node of nodes.get()) {
        node.color = {
            border: config.node_border,  // Color of the border
            background: config.node_bg,  // Color of the background
            highlight: {  // Colors when the node is selected
                border: config.node_highlight_border,  // Color of the border
                background: config.node_highlight_bg,  // Color of the background
            }
        }
        nodes.update(node)
    }
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
    console.log(serializeForm(form))
    form.onsubmit = async (event) => {
        event.preventDefault()
        response = await fetch('api/createModel', {
            method: 'POST',
            body: JSON.stringify(serializeForm(form)),
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
        })
        response = await response.json()
        console.log(response)
    }
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