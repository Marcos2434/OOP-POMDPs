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

        this.sensor_selection = false
        
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

    setBgColor = (c) => this.config = this.configs[c]
    
    styleGraph = () => {
        this.container.style.backgroundColor = this.config.canvas_bg
        const nodeBorderSize = this.config.nodeBorderSize
        for (let node of this.nodes.get()) {
            if (node.id == this.target) {
                node.color = {
                    border: "green",
                    background: this.config.node_bg,
                    highlight: {  // Colors when the node is selected
                        border: "green",
                        background: this.config.node_highlight_bg,
                    }
                }
                node.borderWidth = nodeBorderSize
                node.font = {color: this.config.node_border} // update label color 
                this.nodes.update(node)
                continue
            }
            node.color = {
                border: this.config.node_border,
                background: this.config.node_bg,
                highlight: {  // Colors when the node is selected
                    border: this.config.node_highlight_border,
                    background: this.config.node_highlight_bg,
                }
            }
            node.borderWidth = nodeBorderSize
            node.font = {color: this.config.node_border} // update label color 
            this.nodes.update(node)
        }

        for (let edge of this.edges.get()) {
            edge.color = this.config.edge_color
            // update label color 
            edge.font = {
                color: this.config.edge_color
            }
            this.edges.update(edge)
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
                        let id = i * this.size + j
                        this.nodes.add({ id: id, label: id.toString() })
                        if (i > 0) {
                            this.edges.add({ from: id - this.size, to: id })
                        }
                        if (j > 0) {
                            this.edges.add({ from: id - 1, to: id })
                        }
                    }
                }
                break;
            case "Maze":
                // create the maze model
                if (this.columns % 2 == 0) return // columns must be odd
                for (let i = 0; i < this.rows; i++) {
                    for (let j = 0; j < this.columns; j++) {
                        let id = (i * this.columns) + j
                        if (i == 0) {
                            this.nodes.add({ id, label: id.toString() })
                            if (j != 0) this.edges.add({ from: id - 1, to: id })
                        } else if (j % 2 == 0) {
                            // id = (i * this.columns) + Math.ceil(j / 2)
                            // let nodeOnTop = id - this.columns
                            
                            // id = (i * this.columns) + Math.ceil(j / 2) + ( (i - 1) * Math.ceil(this.columns / 2) - 1 )
                            // let nodeOnTop = id - Math.floor(this.columns / 2)


                            // id = (i * this.columns) + Math.floor(j/2) - (i - 1) * (Math.floor(this.columns / 2)+1)
                            // let nodeOnTop = (i == 1) ? id - (this.columns - 1) + Math.floor(j/2) : id - Math.floor(this.columns / 2)

                            id = this.columns + (i - 1) * Math.ceil(this.columns / 2) + j / 2
                            let nodeOnTop = (i == 1) ? id - this.columns + j / 2 : id - Math.ceil(this.columns / 2)
                        
                            this.nodes.add({ id, label: id.toString() })
                            this.edges.add({ from: id, to: nodeOnTop })
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
                    this.nodes.add({ id: i, 
                        label: this.satelliteNodeData[i] ? i.toString() + (this.satelliteNodeData[i].active ? ', @' : '') : i.toString()
                    })
                    if (this.satelliteNodeData[i]) {
                        // const strategy = this.satelliteNodeData[id].observable
                        const iterable = this.sensor_selection ? this.satelliteNodeData[i] : this.stratInfo[this.satelliteNodeData[i].observable]
                        for (const [action, prob] of Object.entries(iterable.actionProbabilities)) {
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
                        this.nodes.add({ id, label: this.satelliteNodeData[id] ? id.toString() + (this.satelliteNodeData[id].active ? ', @' : '') : id.toString() })
                        
                        if (this.satelliteNodeData[id]) {
                            
                            // const strategy = this.satelliteNodeData[id].observable
                            const iterable = this.sensor_selection ? this.satelliteNodeData[id] : this.stratInfo[this.satelliteNodeData[id].observable]
                            // if (this.stratInfo[strategy]) {
                                for (const [action, prob] of Object.entries(iterable.actionProbabilities)) {
                                    if (i > 0) {
                                        if (action == "up") {
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id - columns, arrows: "to", label: prob.toString(), color: iterable.color })
                                            } else { this.edges.add({ from: id, to: id - columns, arrows: "to"}) }  
                                        } 
                                    }
                                    if (i < rows - 1) {
                                        if (action == "down") {
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id + columns, arrows: "to", label: prob.toString(), color: iterable.color })
                                            } else { this.edges.add({ from: id, to: id + columns, arrows: "to"}) }
                                        }
                                    }
                                    if (j > 0) {
                                        if (action == "left") {
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id - 1, arrows: "to", label: prob.toString(), color: iterable.color })
                                            } else { this.edges.add({ from: id, to: id - 1, arrows: "to"}) }
                                        }
                                    }
                                    if (j < columns - 1) {
                                        if (action == "right") {
                                            // console.log(id, action, prob)
                                            if (prob > 0) {
                                                this.edges.add({ from: id, to: id + 1, arrows: "to", label: prob.toString(), color: iterable.color })
                                            } else { this.edges.add({ from: id, to: id + 1, arrows: "to"}) }
                                        }
                                    }
                                }
                            // } else console.log("strategy not found")
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
            case "Maze":
                for (let i = 0; i < this.rows; i++) {
                    for (let j = 0; j < this.columns; j++) {
                        let id = (i * this.columns) + j
                        if (i == 0) {
                            this.nodes.add({ id, label: this.satelliteNodeData[id] ? id.toString() + (this.satelliteNodeData[id].active ? ', @' : '') : id.toString() })
                            if (j != 0) {
                                this.edges.add({ from: id - 1, to: id, arrows: "to" })
                                this.edges.add({ from: id, to: id - 1, arrows: "to" })
                            }
                        } else if (j % 2 != 0) {
                            id = this.columns + (i - 1) * Math.ceil(this.columns / 2) + j / 2
                            let nodeOnTop = (i == 1) ? id - this.columns + j / 2 : id - Math.ceil(this.columns / 2)
                        
                            this.nodes.add({ id, label: this.satelliteNodeData[id] ? id.toString() + (this.satelliteNodeData[id].active ? ', @' : '') : id.toString() })
                            this.edges.add({ from: id, to: nodeOnTop, arrows: "to" })
                            this.edges.add({ from: nodeOnTop, to: id, arrows: "to" })
                        }
                    }
                }
            
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

    updateNetwork = ({ model, target, size, rows, columns, sensor_selection }) => {
        // set the new parameters
        this.model = model
        this.size = size
        this.target = target
        this.rows = rows
        this.columns = columns
        this.sensor_selection = sensor_selection == "on"

        // reset graph
        this.nodes.clear()
        this.edges.clear()

        // create the new model
        this.createModel()
        this.network.setData({nodes: this.nodes, edges: this.edges})
        this.styleGraph()
    }

    drawSolution = solution => {
        this.solution = solution

        console.log("Solution:")
        console.log(solution)

        let colors = [
            "blue", "magenta", "lime", "olive", "purple", 
            "yellow", "pink", "orange", "red", "cyan", 
        ]

        // Give each observable a colour and update the nodes
        for (const [key, value] of Object.entries(solution)) {
            
            if (!this.sensor_selection) {
                if (key.substring(0, 2) == 'ys') {
                    // In state s, observable o is found, 1 yes, 0 no
                    if (value == 1) {
                        
                        // format key = ys<state>_<observable>
                        const s = parseInt(key.substring(2, key.indexOf('_')))
                        const o = parseInt(key.substring(key.indexOf('_')+1, key.length))

                        // assign a color to each observable and add it to the strategy info object
                        if (!this.stratInfo[o])
                            this.stratInfo[o] = {
                                id: o,
                                color: colors.pop(),
                                actionProbabilities: {
                                    right: 0,
                                    left: 0,
                                    up: 0,
                                    down: 0,
                                }
                            }

                        // add observable to satellite node data so that we know the strategy 
                        // of each node when looping through them
                        this.satelliteNodeData[s] = {observable : o}
                    }
                } 
            } else {
                // Observable / sensor is active on state s
                if (key.substring(0, 1) == 'y') {
                    if (value == 1) {

                        // format key = y<state>
                        const s = parseInt(key.substring(1, key.length))

                        // set the observable to active on the node
                        if (!this.satelliteNodeData[s]) this.satelliteNodeData[s] = {
                            active : true,
                            actionProbabilities: {
                                right: 0,
                                left: 0,
                                up: 0,
                                down: 0,
                            }
                        }
                    }

                }
            }
        }

        // Once each observable has been mapped to a colour, update the strategy table
        for (const [key, value] of Object.entries(solution)) {
            if (!this.sensor_selection) {
                if (key.substring(0, 2) == 'xo') {
                    const o = parseInt(key[2]) // o for observable
                    const a = key[3] // a for action

                    if (!this.stratInfo[o]) continue
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
            } else {
                if (key.substring(0, 2) == 'xo') {

                    // format : xo<observable><action>
                    // since action is always the last character, we can infer that the
                    // observable goes from the third character to the second to last character
                    const s = parseInt(key.substring(2, key.length - 1)) // o for observable
                    const a = key[key.length - 1] // a for action

                    if (!this.satelliteNodeData[s]) this.satelliteNodeData[s] = {
                        active: false,
                        actionProbabilities: {
                            right: 0,
                            left: 0,
                            up: 0,
                            down: 0,
                        }
                    }

                    switch (a) {
                        case 'l':
                            this.satelliteNodeData[s].actionProbabilities.left = value
                            break
                        case 'r':
                            this.satelliteNodeData[s].actionProbabilities.right = value
                            break
                        case 'u':
                            this.satelliteNodeData[s].actionProbabilities.up = value
                            break
                        case 'd':
                            this.satelliteNodeData[s].actionProbabilities.down = value
                            break
                    }
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

        console.log("Strat Info:")
        console.log(this.stratInfo)
        console.log("Satellite Node Data:")
        console.log(this.satelliteNodeData)

        this.createDirectedModel()
    }
}
