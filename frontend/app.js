const api = "http://localhost:8000/api";
async function fetchStatus() {
  const res = await fetch(`${api}/status`);
  const data = await res.json();
  document.getElementById("temp").textContent = data.temperature;
  document.getElementById("crying").textContent = data.baby_crying ? "Yes 😢" : "No 😊";
  document.getElementById("light").textContent = data.light;
}
async function toggleLight() {
  const res = await fetch(`${api}/toggle-light`, { method: "POST" });
  alert("Light toggled!");
  fetchStatus();
}
setInterval(fetchStatus, 5000);
fetchStatus();