import csv

def write_passages_to_csv(passages):
    with open("passages.csv", 'w') as f_out:
        out_colnames = ["passage id", "document id", "keyword", "content", "prior-context", "after-context"]
        csv_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        csv_writer.writeheader()
        for row in passages:
            csv_writer.writerow(row)

def write_documents_to_csv(documents):
    with open("documents.csv", 'w') as f_out:
        out_colnames = ['document id', 'keyword', 'document title', 'document publication date', 'document path', 'word count']
        csv_writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        csv_writer.writeheader()
        for row in documents:
            csv_writer.writerow(row)
    