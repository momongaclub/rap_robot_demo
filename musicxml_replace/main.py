import sys
import argparse
import xml.etree.ElementTree as ET


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('music_xml',
                        help = 'target music_xml')
    parser.add_argument('replace_text',
                        help = 'replace_text')
    parser.add_argument('output_xml',
                        help = 'output_xml')
    args = parser.parse_args()
    return args


def load_replace_tokens(fname):
    tokens = []
    with open(fname, 'r') as fp:
        sentence = fp.readline()
        for token in sentence:
            tokens.append(token)
    print(tokens)
    return tokens


def main():
    args = parse()
    tokens = load_replace_tokens(args.replace_text)
    tree = ET.parse(args.music_xml)
    root = tree.getroot()
    cnt = 0
    for part in root.findall('part'):
        for measure in part.findall('measure'):
            for note in measure.findall('note'):
                for lyric in note.findall('lyric'):
                    for text in lyric.findall('text'): # zipでいいのか
                        try:
                            print('text', text.text, 'token', tokens[cnt])
                            text.text = str(tokens[cnt])
                            cnt += 1
                        except:
                            tree.write(args.output_xml, "utf-8")
                            return 0
    tree.write(args.output_xml, "utf-8")

if __name__ == '__main__':
    main()
