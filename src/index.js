import { Trinity, helpers } from 'trinity-web'

import TrinityDOM from 'trinity-dom'
import ApiClient from 'trinity-plugin-api'

import { Home, Admin } from './containers'

const initialStore =  window.__data ? JSON.parse(window.__data) : {}

const app = new Trinity('app', initialStore)

helpers.dom.addHeadTags(
  'App',
  { tag: 'link', href: 'pub/assets/css/trinity.css' }
)

app.context('render', TrinityDOM(require('./utils/dom.js')))
app.context('api', new ApiClient('http://localhost:5000'))

if (window.__page) {
  app.redirect(window.__page)
}

app.route('/', Home)
app.route('/login', Admin.Login)

app.start()
