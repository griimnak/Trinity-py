import superagent from 'superagent'

const methods = ['get', 'post', 'put', 'patch', 'del']

export default class ApiClient {

  formatUrl(path) {
    const adjustedPath = path[0] !== '/' ? `/${path}` : path
    // Prepend `/api` to relative URL, to proxy to API server.
    return this.url + adjustedPath
  }

  constructor(url) {
    this.url = url

    methods.forEach(method => {
      this[method] = (path, { params, data, headers, files, fields } = {}) =>
        new Promise((resolve, reject) => {
          const request = superagent[method](this.formatUrl(path))

          if (params) {
            request.query(params)
          }

          if (window.__csrf_token) {
            request.set('X-CSRF-Token', window.__csrf_token)
          }

          if (headers) {
            request.set(headers)
          }

          if (this.token) {
            request.set('Authorization', `Bearer ${this.token}`)
          }

          if (files) {
            files.forEach(file => request.attach(file.key, file.value))
          }

          if (fields) {
            fields.forEach(item => request.field(item.key, item.value))
          }

          if (data) {
            request.send(data)
          }

          request.end((err, { body } = {}) => (err ? reject(body || err) : resolve(body)))
        })
    })
  }

  setJwtToken(token) {
    this.token = token
  }
}
