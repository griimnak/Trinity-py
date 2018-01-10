import webpack from 'webpack'
import path from 'path'

const appName = 'Trinity3'
const trinityPath = path.join(__dirname, '..', 'js')
const outputFile = 'bundle.min.js'

export default {
  devtool: 'inline-source-map',
  entry: [
    'babel-polyfill',
    trinityPath,
  ],
  output: {
    path: path.resolve(__dirname, '..', 'pub', 'js'),
    filename: outputFile,
    library: appName,
    libraryTarget: 'umd',
    umdNamedDefine: true,
    //publicPath
  },
  module: {
    rules: [
      {
        test: /(\.jsx|\.js)$/,
        include: path.join(__dirname, '..', 'js'),
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    modules: [
      path.resolve(__dirname, '..', 'js'),
      'node_modules'
    ],
    extensions: ['.json', '.js']
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NamedModulesPlugin(),
    new webpack.optimize.UglifyJsPlugin({ minimize: true })
  ]
}
