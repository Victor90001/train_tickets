async function getStation(e){
    stations = e.target.list
    if (stations.innerHTML.trim() == ''){
        const response = getStations(e.target)
        await response.then((values)=>addStations(values))
    }
}

async function updateStation(e){
    stations = e.target.list
    input = document.getElementById(e.target.id+"Id")
    console.log(input.value)
    const response = getStations(e.target)
    await response.then((values)=>addStations(values))
    const arr = [...stations.children]
    arr.forEach(element =>{
        if (element.value == e.target.value){
            input.value = element.id
        }
    })
}

async function getStations(v){
    const value = v.value
    const stationsdata = v.list
    const params = new URLSearchParams()
    if (value.length > 0){
        params.append('part', value)
    }
    const response = await fetch("fetch?"+params)
    const stations = await response.json()
    await clearStations(stationsdata)
    return stations
}

async function addStations(v){
    v[1].forEach(element => {
        var option = document.createElement('option')
        option.value = element[1]
        option.text = element[2]
        option.id = element[0]
        stations.appendChild(option)
    });
}

async function clearStations(d){
    d.innerHTML = ''
}

document.addEventListener('DOMContentLoaded', (e)=>{
    const frominput = document.getElementById("inputFrom")
    const toinput = document.getElementById("inputTo")
    const dateinput = document.getElementById("inputDate")

    const datastationfrom = document.getElementById("stationsfrom")
    const datastationto = document.getElementById("stationsto")

    frominput.addEventListener("focus", getStation)
    frominput.addEventListener("input", updateStation)

    toinput.addEventListener("focus", getStation)
    toinput.addEventListener("input", updateStation)
    
})
