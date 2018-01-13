import webpack from 'webpack'
import path from 'path'

const appName = 'Trinity3'
const trinityPath = path.resolve(__dirname, '..', 'src')
const outputFile = 'trinity3.min.js'

export default {
  devtool: 'inline-source-map',
  entry: trinityPath,
  output: {
    path: path.resolve(__dirname, '..', 'pub', 'assets', 'js'),
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
        include: trinityPath,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    modules: [
      trinityPath,
      'node_modules'
    ],
    extensions: ['.json', '.js']
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({ minimize: true })
  ]
}
