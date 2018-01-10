import webpack from 'webpack'
import path from 'path'

const port = process.env.WEBPACK_PORT || 9000
const publicPath = `http://localhost:${port}/dist/`
//const env = process.env.WEBPACK_ENV
const appName = 'Trinity3'
const plugins = []

const trinityPath = path.join(__dirname, '..', 'test', 'index.js')
const outputFile = appName.toLowerCase() + '.js'

const testPath = path.join(__dirname, '..', 'test')
const srcPath = path.resolve(__dirname, '..', 'src')

export default {
  devtool: 'inline-source-map',
  entry: [
    'babel-polyfill',
    `webpack-hot-middleware/client?path=http://localhost:${port}/__webpack_hmr`,
    trinityPath,
  ],
  output: {
    path: path.resolve(__dirname, '..', 'dist'),
    filename: outputFile,
    library: appName,
    libraryTarget: 'umd',
    umdNamedDefine: true,
    publicPath
  },
  module: {
    rules: [
      {
        test: /(\.jsx|\.js)$/,
        include: [testPath, srcPath],
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    modules: [
      testPath,
      srcPath,
      'node_modules'
    ],
    extensions: ['.json', '.js']
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    //new WatchMissingNodeModulesPlugin(paths.appNodeModules),
    new webpack.NamedModulesPlugin(),
    //new webpack.optimize.UglifyJsPlugin(/*{ minimize: true }*/)
  ]
}
