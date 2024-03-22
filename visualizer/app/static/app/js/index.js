document.addEventListener("DOMContentLoaded", () => {
    const mobileNav = document.querySelector(".hamburger")
    mobileNav.addEventListener("click", toggleNav)

    modelFormHandler()
})

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

const modelFormHandler = () => {
    form = document.querySelector('#oop_form')
    let form_data = serializeForm(form)
    let networkData = new NetworkData({model: form_data.model, size: parseInt(form_data.size), target: parseInt(form_data.target)})

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
            console.log(data.solution)
            console.log(form_data)
            networkData.updateNetwork({model: form_data.model, size : parseInt(form_data.size), target: parseInt(form_data.target)})
            networkData.drawSolution(data.solution)
        } else {
            console.error(response)
            alert("Error: " + response.status + "\n" + response.statusText)
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