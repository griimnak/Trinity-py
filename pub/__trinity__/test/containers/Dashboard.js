import { Container } from '../../src'

export default class Dashboard extends Container {

  routeWillLeave = ({ store }) => {
    // clean up process like remove user from store
    store.setState({ lastPage: 'Dashboard' })
  }

  render = ({ props }) => ({
    selector: 'app',
    html: `
      <a href="/" data-navigate>
        test
      </a>
    `
  })

}
