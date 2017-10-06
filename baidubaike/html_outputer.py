class HtmlOutputer(object):
    
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):

        if data is None:
            return
        self.datas.append(data)



    def output_html(self):
        with open('output.html', 'w', encoding='utf-8'):
            fout.write('<html>')
            fout.write('<body>')
            fout.write('<table>')
        
            for data in self.datas:
                fout.write('<tr>')
                fout.write('<h1>%s</h1>' % data['title'])
                fout.write('<h2>%s</h2>' % data['url'])
                fout.write('<h4>%s</h4>' % data['summary'])
                fout.write('</tr>')

            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')
