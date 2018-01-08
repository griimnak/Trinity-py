import { Component } from '../../src'

export default class LastPage extends Component {

  beforeMount = () => ({
    action: (api) => api.get('https://www.mocky.io/v2/5185415ba171ea3a00704eed'),
    html: `<div>Loading</div>`
  })

  render = ({ props }) => ({
    html: `<a href="/dashboard" data-navigate> ${props.store.getState().lastPage}</a>`
  })
}