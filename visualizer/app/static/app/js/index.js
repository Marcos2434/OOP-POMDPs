document.addEventListener("DOMContentLoaded", () => {

    // Responsive menu bar
    const mobileNav = document.querySelector(".hamburger")
    mobileNav.addEventListener("click", toggleNav)

    // Handle form inputs and outputs to update graph
    modelFormHandler()
})

const modelFormHandler = () => {
    form = document.querySelector('#oop_form')
    let form_data = serializeForm(form)
    let networkData = new NetworkData({model: form_data.model, size: parseInt(form_data.size), target: parseInt(form_data.target)})

    let controller;

    form.addEventListener('submit', async event => {
        if (controller) controller.abort()
        
        event.preventDefault()

        controller = new AbortController()
        
        const loader = document.querySelector("#loader")
        loader.classList.remove("disappear")
        
        const counter = document.querySelector("#counter")
        counter.innerHTML = 0
        const increaseCounter = () => counter.innerHTML = parseInt(counter.innerHTML) + 1
        const counterInterval = setInterval(increaseCounter, 1000)

        const signal = controller.signal

        try {
            const response = await fetch('api/createModel', {
                method: 'POST',
                body: JSON.stringify(serializeForm(form)),
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                signal,
            })
            const data = await response.json()
            console.log(data)

            clearInterval(counterInterval)
            loader.classList.add("disappear")

            if (data.solution == "No solution") {
                alert("No solution found for the given model")
                return
            } else if (data.solution == "Unknown") {
                alert("Unknown error")
                return
            }

            networkData.updateNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
            networkData.drawSolution(data.solution)
        } catch (error) {
            clearInterval(counterInterval)
            loader.classList.add("disappear")
            if (error.name == "AbortError") {
                console.log("Request aborted")
            } 
            else {
                console.error(error)
            }
            return
        }
    })

    
    form.addEventListener('change', event => {
        form_data = serializeForm(form)
            networkData.updateNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
    })

    document.querySelector("#theme-select").addEventListener("change", e => {
        networkData.updateNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
        networkData.setBgColor(e.target.value)
        // networkData = handleNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
        // handleNetwrokContainerColor();
    })
}

const aspectRatio = () => {
    const network_canvas = document.querySelector("#network");
    const styles = getComputedStyle(network_canvas);
    network_canvas.style.height = styles.width;
    window.addEventListener("resize", () => network_canvas.style.height = styles.width);
}

const toggleNav = () => {
    const navbar = document.querySelector(".menubar");
    const mobileNav = document.querySelector(".hamburger");
    navbar.classList.toggle("active");
    mobileNav.classList.toggle("hamburger-active");
}

const serializeForm = form => {
    // Serialize form data into JSON object
    const formData = new FormData(form)
    const data = {}
    for (const [key, value] of formData.entries()) {
        data[key] = value
    }
    return data
}

// Get CSRF token for POST requests, Django
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