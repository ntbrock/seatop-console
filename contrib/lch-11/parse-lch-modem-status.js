var reverseMustache = require('reverse-mustache');

var debug = false;

var tmpl = "<html><head><title>Modem Status</title> \r\n" + 
"<style type=\"text/css\">div.output{margin:2px 2px 2px 4px;padding:0 0 0 0}body{margin:0;padding:0}table,td{padding:2px;margin:0;font:normal 9pt/9pt 'Courier New',Courier,serif}</style></head><body lang=\"en\"> <div class=output>\r\n" + 
"<div class=output> <table> <tbody> <tr>\n" + 
"<td nowrap>MDN:</td> <td nowrap>{{mdn}}</td></tr><tr> <td nowrap>ESN (hex):</td> <td nowrap>{{esn}}</td></tr> <tr> <td nowrap>Channel:</td>\n" + 
"<td nowrap>{{channel}}</td></tr> <tr> <td nowrap>P_REV Indicator:</td> <td nowrap>{{p_rev}}</td></tr> <tr> <td nowrap>PRL ID:</td>\n" + 
"<td nowrap>{{prl_id}}</td></tr> <tr> <td nowrap>Band Class Type:</td> <td nowrap>{{band_class}}</td></tr> <tr> <td nowrap>ERI Version:</td>\n" + 
"<td nowrap>{{eri_version}}</td></tr> <tr> <td nowrap>Dormancy:</td> <td nowrap>{{dormancy}}</td></tr> <tr> <td nowrap>Signal - EVDO:</td>\n" + 
"<td nowrap>{{signal_evdo}}</td></tr> <tr> <td nowrap>Signal - LTE:</td> <td nowrap>{{signal_lte}}</td></tr> <tr> <td nowrap>Battery Level:</td>\n" + 
"<td nowrap>{{battery_level}}</td></tr> <tr> <td nowrap>Battery Charging:</td> <td nowrap>{{battery_charging}}</td></tr> </tbody> </table></div></body></html>"

// small input
//tmpl = "<td nowrap>{{mdn}}</td></tr>"

// small input 2
//tmpl = "<td nowrap>MDN:</td> <td nowrap>{{mdn}}</td></tr><tr> <td nowrap>ESN (hex):</td> <td nowrap>{{esn}}</td></tr> <tr> <td nowrap>Channel:</td>"

// small input 3
//tmpl = "<td nowrap>MDN:</td> <td nowrap>{{mdn}}</td></tr><tr> <td nowrap>ESN (hex):</td> <td nowrap>{{esn}}</td></tr> <tr> <td nowrap>Channel:</td>\n" + "<td nowrap>{{channel}}</td></tr> <tr> <td nowrap>P_REV Indicator:</td> <td nowrap>{{p_rev}}</td></tr> <tr> <td nowrap>PRL ID:</td>"


var input = '';
process.stdin.resume();
process.stdin.setEncoding('utf8');
process.stdin.on('data', function (chunk) {
    input = input + chunk.trim();
    // process.stdout.write('data: ' + chunk);
});

process.stdin.on('end', function() { 

if ( debug ) { 
    console.log("------ parse-lch-modem ---[Input]--------\n" + input);
    console.log("------ parse-lch-modem ---[Template]-----\n" + tmpl);
}

    var result = reverseMustache({
	template: tmpl, // 'hello {{#place}}world{{/place}}',
	content: input
    });

if ( debug ) { 
    console.log("------ parse-lch-modem ---[Result]-------\n",  result);
} else { 
    console.log(result);
}

})
