// Author: Anubiri Chika Anselem

const API = "http://127.0.0.1:5000";


async function getStudent() {

    const id = document.getElementById("studentId").value;

    if (!id) {
        alert("Enter student ID");
        return;
    }

    const res = await fetch(${API}/student/${id});
    const data = await res.json();

    document.getElementById("result").textContent =
        JSON.stringify(data, null, 2);
}


async function getStats() {

    const res = await fetch(${API}/stats);
    const data = await res.json();

    document.getElementById("stats").textContent =
        JSON.stringify(data, null, 2);
}


async function clearCache() {

    await fetch(${API}/clear);
    alert("Cache Cleared");

    getStats();
}


// Auto refresh stats every 5 seconds
setInterval(getStats, 5000);

