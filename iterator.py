import json

class CountriesWikiURLs:

    def __init__(self, json_file, output_file):
        self.start = 0
        self.json_file = json_file
        self.output_file = output_file
        with open(json_file, 'r', encoding='utf-8') as f:
            self.countries_data_list = json.load(f)
        self.end = len(self.countries_data_list)
        start_text = '<!DOCTYPE html>' + '\n' + '<html lang="en">' + '\n' + '<head>' + '\n' + '    ' + '<meta charset="UTF-8">' + '\n' + '    ' + '<title>Title</title>' + '\n' + '</head>' + '\n' + '<body>'
        with open(self.output_file, 'a', encoding='utf-8') as file:
            file.write(start_text + '\n')

    def __iter__(self):

        return self

    def __next__(self):

        self.country = self.countries_data_list[self.start]['name']['common']
        self.country = self.country.replace(' ', '_')

        text_line = f'<p>{self.country} - <a href = "https://en.wikipedia.org/wiki/{self.country}">{self.country}</a></p>'

        with open(self.output_file, 'a', encoding='utf-8') as file:
            file.write(text_line + '\n')
        self.start += 1
        if self.start == self.end:
            end_text = '</body>' + '\n' + '</html>'
            with open(self.output_file, 'a', encoding='utf-8') as file:
                file.write(end_text + '\n')
            raise StopIteration
        return self.start


if __name__ == '__main__':
    for country in CountriesWikiURLs('countries.json', 'countries wiki URLs.html'):
        pass