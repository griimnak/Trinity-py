$(document).ready(function () {
    /*
    * SPARKLINE
    */
    function sparklineBar(id, height, barWidth, barColor, barSpacing) {
        $('.'+id).sparkline('html', {
            type: 'bar',
            height: height,
            barWidth: barWidth,
            barColor: barColor,
            barSpacing: barSpacing
        })
    }
    
    function sparklineLine(id, width, height, lineColor, fillColor, lineWidth, maxSpotColor, minSpotColor, spotColor, spotRadius, hSpotColor, hLineColor) {
        $('.'+id).sparkline('html', {
            type: 'line',
            width: width,
            height: height,
            lineColor: lineColor,
            fillColor: fillColor,
            lineWidth: lineWidth,
            maxSpotColor: maxSpotColor,
            minSpotColor: minSpotColor,
            spotColor: spotColor,
            spotRadius: spotRadius,
            highlightSpotColor: hSpotColor,
            highlightLineColor: hLineColor
        });
    }
    
    if ($('.overview-chart-line')[0]) {
        sparklineLine('overview-chart-line', '100%', 50, 'rgba(255,255,255,0.6)', 'rgba(0,0,0,0)', 1.5, '#fff', '#fff', '#fff', 5, '#fff', '#fff');
    }
    
    if ($('.overview-chart-bar')[0]) {
        sparklineBar('overview-chart-bar', 50, 4, 'rgba(255,255,255,0.9)', 2);
    }
    
    /*----------------------------------------------------------
        Easy Pie Charts
    -----------------------------------------------------------*/
    function easyPieChart(id, barColor, trackColor, scaleColor, lineWidth, size) {
        $('.'+id).easyPieChart({
            easing: 'easeOutBounce',
            barColor: barColor,
            trackColor: trackColor,
            scaleColor: scaleColor,
            lineCap: 'square',
            lineWidth: lineWidth,
            size: size,
            animate: 3000,
            onStep: function(from, to, percent) {
                $(this.el).find('.percent').text(Math.round(percent));
            }
        });
    }
    
    easyPieChart('pie-chart-tiny', '#fff', 'rgba(0,0,0,0.08)', 'rgba(0,0,0,0)', 3, 100);
    
      
});