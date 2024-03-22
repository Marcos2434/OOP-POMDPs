class NetworkData {
    constructor({model, size = 1, rows = 1, columns = 1, target}) {

        this.nodes = new vis.DataSet()
        this.satelliteNodeData = {}
        this.edges = new vis.DataSet()
        this.target = target
        this.model = model
        this.size = size
        this.rows = rows
        this.columns = columns
        
        this.tableBodyRef = document.querySelector("#strat-table").querySelector("tbody")

        this.configs = {
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

        this.config = this.configs.transparent

        const options = {
            autoResize: true,
            height: '100%',
            width: '100%',
            locale: 'en',
            clickToUse: false,
            configure: {},    // defined in the configure module.
            edges: {
                color: {
                    color: this.config.edge_color,
                    inherit: false, // Disable color inheritance
                    opacity: 1.0
                },
                font: {
                    size: 25,
                    color: "white",
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
                    color: this.config.node_font_color,
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
            }, // defined in the physics module.
        }
        
        this.container = document.querySelector("#network")
        this.setBgColor("transparent")

        this.createModel()
        this.styleGraph()
        this.network = new vis.Network(this.container, {nodes: this.nodes, edges: this.edges}, options);


        // handle download button
        this.network.on("afterDrawing", ctx => {
            let dataURL = ctx.canvas.toDataURL();
            document.getElementById('downloadButton').onclick = () => {
            let link = document.createElement('a')
            link.download = 'network.png'
            link.href = dataURL
            link.click()
            }
        })

        this.stratInfo = {}
    }

    setBgColor = (c) => {
        this.config = this.configs[c]
        this.container.style.backgroundColor = this.config.canvas_bg
    }

    styleGraph = () => {
        const nodeBorderSize = this.config.nodeBorderSize
        for (let node of this.nodes.get()) {
            if (node.id == this.target) {
                node.color = {
                    border: "green",  // Color of the border
                    background: this.config.node_bg,  // Color of the background
                    highlight: {  // Colors when the node is selected
                        border: "green",  // Color of the border
                        background: this.config.node_highlight_bg,  // Color of the background
                    }
                }
                node.borderWidth = nodeBorderSize
                this.nodes.update(node)
                continue
            }
            node.color = {
                border: this.config.node_border,  // Color of the border
                background: this.config.node_bg,  // Color of the background
                highlight: {  // Colors when the node is selected
                    border: this.config.node_highlight_border,  // Color of the border
                    background: this.config.node_highlight_bg,  // Color of the background
                }
            }
            node.borderWidth = nodeBorderSize
            this.nodes.update(node)
        }
    }

    createModel = () => {
        switch (this.model) {
            case "Line":
                // create the line model
                for (let i = 0; i < this.size; i++) {
                    this.nodes.add({ id: i, label: i.toString() });
                    if (i > 0) {
                        this.edges.add({ from: i - 1, to: i });
                    }
                }
                break;
            case "Grid":
                // create the grid model
                for (let i = 0; i < this.size; i++) {
                    for (let j = 0; j < this.size; j++) {
                        let id = i * this.size + j;
                        this.nodes.add({ id: id, label: id.toString() });
                        if (i > 0) {
                            this.edges.add({ from: id - this.size, to: id });
                        }
                        if (j > 0) {
                            this.edges.add({ from: id - 1, to: id });
                        }
                    }
                }
                break;
            case "Maze":
                // create the maze model
                for (let i = 0; i < this.size; i++) {
                    for (let j = 0; j < this.size; j++) {
                        let id = i * this.size + j;
                        this.nodes.add({ id: id, label: id.toString() });
                        if (i > 0) {
                            this.edges.add({ from: id - this.size, to: id });
                        }
                        if (j > 0) {
                            this.edges.add({ from: id - 1, to: id });
                        }
                    }
                }
                break;
        }
    }

    createDirectedModel = () => {
        // recreate grid model with directed edges
        // remove all nodes and edges
        this.nodes.clear()
        this.edges.clear()
        switch (this.model) {
            case "Line":
                // create directed line model size
                for (let i = 0; i < this.size; i++) {
                    this.nodes.add({ id: i, label: i.toString() })
                    if (this.satelliteNodeData[i]) {
                        const strategy = this.satelliteNodeData[i].observable
                        for (const [action, prob] of Object.entries(this.stratInfo[strategy].actionProbabilities)) {
                            switch (action) {
                                case "right":
                                    if (i < this.size - 1 && prob > 0) this.edges.add({ from: i, to: i + 1, arrows: "to", label: prob.toString() });
                                    else this.edges.add({ from: i, to: i + 1, arrows: "to" })
                                    break
                                case "left":
                                    if (i > 0 && prob > 0) this.edges.add({ from: i, to: i - 1, arrows: "to", label: prob.toString() });
                                    else this.edges.add({ from: i, to: i - 1, arrows: "to" })
                                    break
                            }   
                        }
                    } else {
                        this.edges.add({ from: i, to: i + 1, arrows: "to" })
                        this.edges.add({ from: i, to: i - 1, arrows: "to" })
                    }               
                
                }
                break;
            case "Grid":
                // crete directed grid model size x size
                let rows = this.size
                let columns = this.size
                for (let i = 0; i < rows; i++) {
                    for (let j = 0; j < columns; j++) {
                        let id = i * columns + j
                        this.nodes.add({ id: id, label: id.toString() })
                        
                        if (this.satelliteNodeData[id]) {
                            const strategy = this.satelliteNodeData[id].observable
                            if (this.stratInfo[strategy]) {
                                for (const [action, prob] of Object.entries(this.stratInfo[strategy].actionProbabilities)) {
                                    if (i > 0) {
                                        if (action == "up") {
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id - columns, arrows: "to", label: prob.toString(), color: this.stratInfo[strategy].color })
                                            } else { this.edges.add({ from: id, to: id - columns, arrows: "to"}) }  
                                        } 
                                    }
                                    if (i < rows - 1) {
                                        if (action == "down") {
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id + columns, arrows: "to", label: prob.toString(), color: this.stratInfo[strategy].color })
                                            } else { this.edges.add({ from: id, to: id + columns, arrows: "to"}) }
                                        }
                                    }
                                    if (j > 0) {
                                        if (action == "left") {
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id - 1, arrows: "to", label: prob.toString(), color: this.stratInfo[strategy].color })
                                            } else { this.edges.add({ from: id, to: id - 1, arrows: "to"}) }
                                        }
                                    }
                                    if (j < columns - 1) {
                                        if (action == "right") {
                                            // console.log(id, action, prob)
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id + 1, arrows: "to", label: prob.toString(), color: this.stratInfo[strategy].color })
                                            } else { this.edges.add({ from: id, to: id + 1, arrows: "to"}) }
                                        }
                                    }
                                }
                            }
                        } else {
                            if (i > 0) {
                                this.edges.add({ from: id, to: id - columns, arrows: "to"})
                            }
                            if (i < rows - 1) {
                                this.edges.add({ from: id, to: id + columns, arrows: "to"})
                            }
                            if (j > 0) {
                                this.edges.add({ from: id, to: id - 1, arrows: "to"})
                            }
                            if (j < columns - 1) {
                                this.edges.add({ from: id, to: id + 1, arrows: "to"})
                            }
                        }

                    }
                }
                break
            
        }

        this.styleGraph()
        // color solution onto graph
        for (let node of this.nodes.get()) {
            if (this.satelliteNodeData[node.id]) {
                const strategy = this.satelliteNodeData[node.id].observable
                if (this.stratInfo[strategy] != null) {
                    node.color = {
                        border: this.stratInfo[strategy].color,
                        background: this.config.node_bg,
                        highlight: {
                            border: this.stratInfo[strategy].color,
                            background: this.config.node_highlight_bg,
                        }
                    }
                    this.nodes.update(node)
                }
            }
        }
    }

    updateNetwork = ({ model, size, target }) => {
        // set the new parameters
        this.model = model
        this.size = size
        this.target = target

        // reset graph
        this.nodes.clear()
        this.edges.clear()

        // create the new model
        this.createModel()
        this.network.setData({nodes: this.nodes, edges: this.edges})
        this.styleGraph()
    }

    drawSolution = (solution) => {
        this.solution = solution

        const colors = [
            "blue", "magenta", "lime", "olive", "purple", 
            "yellow", "pink", "orange", "red", "cyan", 
        ]
        let availableColors = colors
        let observableColors = {}

        // Give each observable a colour and update the nodes
        for (const [key, value] of Object.entries(solution)) {
            
            if (key.substring(0, 2) == 'ys') {

                // In state s, observable o is found, 1 yes, 0 no
                if (value == 1) {
                    
                    // format key = ys<state>_<observable>

                    // check order of magnitude of budget in the tens
                    // s equals from 2 to "_"
                    const s = parseInt(key.substring(2, key.indexOf('_')))
                    const o = parseInt(key.substring(key.indexOf('_')+1, key.length))

                    if (!this.stratInfo[o]) {
                        this.stratInfo[o] = {
                            id: o,
                            color: observableColors[o],
                            nodes: [],
                            actionProbabilities: {
                                right: 0,
                                left: 0,
                                up: 0,
                                down: 0,
                            }
                        }
                    }

                    // add observable to satellite node data so that we know the strategy 
                    // of each node when looping through each of them
                    if (!this.satelliteNodeData[s]) {
                        this.satelliteNodeData[s] = {
                            observable: o,
                        }
                    }
                    // console.log(s, o, this.satelliteNodeData[s])
                    
                    // Check if the observable has already been mapped to a colour
                    if (!this.stratInfo[o].color) this.stratInfo[o].color = availableColors.pop()
                }
            }
        }

        
        // Once each observable has been mapped to a colour, update the strategy table
        for (const [key, value] of Object.entries(solution)) {
            if (key.substring(0, 2) == 'xo') {
                const o = parseInt(key[2]) // o for observable
                const a = key[3] // a for action

                switch (a) {
                    case 'l':
                        this.stratInfo[o].actionProbabilities.left = value
                        break
                    case 'r':
                        this.stratInfo[o].actionProbabilities.right = value
                        break
                    case 'u':
                        this.stratInfo[o].actionProbabilities.up = value
                        break
                    case 'd':
                        this.stratInfo[o].actionProbabilities.down = value
                        break
                }
            }
        }
        
        
        // Clear table
        this.tableBodyRef.innerHTML = ""
        
        for (const [_, info] of Object.entries(this.stratInfo)) {
            const row = this.tableBodyRef.insertRow(-1)
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

        this.createDirectedModel()
    }

    
}
