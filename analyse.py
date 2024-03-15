from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Invoice:
    supplier: str
    number: str


def sample_data():
    return [
        Invoice('ALP1', 'AB012'),
        Invoice('ALP1', 'AB015'),
        Invoice('ALP1', 'AB020'),
        Invoice('ALP1', 'CF3'),
        Invoice('BET1', 'JJ088'),
        Invoice('BET1', 'JJ199'),
    ]


def supplier_profile():
    invoices = sample_data()
    invoices_profile = defaultdict(dict)
    reference_count = defaultdict(int)

    for invoice in invoices:
        reference_count[invoice.supplier] += 1

    for invoice in invoices:
        reference = invoice.supplier
        number = invoice.number

        frequency, percentage = invoices_profile[reference].get(len(number), (0, 0))
        frequency += 1
        percentage = (frequency / reference_count.get(invoice.supplier)) * 100
        invoices_profile[reference][len(number)] = (frequency, percentage)

    print(f"Analysing {len(invoices)} invoices for task")
    print("Supplier Reference        Invoice Number Length           Frequency           Percentage")
    for supplier, lengths in invoices_profile.items():
        for length, data in lengths.items():
            print(f'{supplier}                      {length}                               {data[0]}                   {data[1]:.2f}%')


if __name__ == "__main__":
    supplier_profile()
