export default function fetch(url) {
  return new Promise((resolve, reject) => {
    const req = new XMLHttpRequest()
    req.open('GET', url)
    req.send()
    req.onload = () => resolve(req.responseText)
    req.onerror = () => reject(req.responseText)
  })
}
