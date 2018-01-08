import { Container } from '../../src'

export default class Github extends Container {

  // props
  // state
  getInitialState = ({ props, store }) => ({
    active: false
  })

  onButtonClick = (event) => this.setState({ active: !this.state.active })

  events = () => ([
    {
      handler: 'click',
      selector: '#active',
      action: this.onButtonClick
    }
  ])

  routeWillLeave = ({ store }) => {
    // clean up logic like remove user from store if logout
    store.setState({ lastPage: 'Github' })
  }

  beforeMount = async ({ api, store, props }) => {
    this._elementRender(props.parent, '<div>Loading</div>')

    try {
      const { data } = await api.get('https://www.mocky.io/v2/5185415ba171ea3a00704eed')

      store.setState({ mocky: { result: data } })
    } catch (error) {
      store.setState({ mocky: { error } })
    }
  }

  render = ({ store, props }) => {
    const { mocky } = store.getState()

    return {
      selector: props.parent,
      html: mocky.result ? mocky.result : mocky.error
    }
  }

}
