<?php
function save()
{
    $items = $_POST['items'];
    $size = $_POST['size'];
    $qty = $_POST['qty'];
    $disc = $_POST['disc'];
    $harga = 0;
    $bayar =0;
    $pajak =0;
    $total =0;
    $myfile = fopen("struk.txt", "w") or die("Unable to open file!");
    $txt = "";
    $txt = $txt . "+====================BL STORE===================+\n";
    $txt = $txt . "                PATLISAN_2011600315              \n";
    $txt = $txt . "+==========+=====+=====+=======+=====+==========+\n";
    $txt = $txt . "|Items     |Size |Qty  |Price  | Dsc | Subtotal |\n";
    $txt = $txt . "+==========+=====+=====+=======+=====+==========+\n";
    foreach ($items as $key => $n) {
        $harga=0;
        $totaldisc =0;
        $subtotal=0;
        if ($n == "Toshiba" && $size[$key] == "1TB") {
            $harga = 50;
           
        }
        if ($n == "Toshiba" && $size[$key] == "2TB") {
            $harga = 75;
           
        }
        if ($n == "Toshiba" && $size[$key] == "4TB") {
            $harga = 150;
           
        }
        if ($n == "Samsung" && $size[$key] == "1TB") {
            $harga = 50;
          
        }
        if ($n == "Samsung" && $size[$key] == "2TB") {
            $harga = 70;
           
        }
        if ($n == "Samsung" && $size[$key] == "4TB") {
            $harga = 145;
          
        }
        if ($n == "Seagate" && $size[$key] == "1TB") {
            $harga = 51;
          
        } if ($n == "Seagate" && $size[$key] == "2TB") {
            $harga = 73;
          
        } if ($n == "Seagate" && $size[$key] == "4TB") {
            $harga = 152;
          
        }

        $totaldisc =($harga*$qty[$key])*($disc[$key]/100);
        $subtotal =($harga*$qty[$key])-$totaldisc;
        $total =$total +$subtotal;
        if($qty[$key]!=''||$qty[$key]!=0){
        $txt = $txt . "|" . $n . "   |" . $size[$key] . "  |".str_pad(number_format($qty[$key],2), 5, ' ', STR_PAD_LEFT) . "|" .str_pad( number_format($harga,2), 7, ' ', STR_PAD_LEFT) . "|".str_pad( $disc[$key], 5, ' ', STR_PAD_LEFT) ."|".str_pad(number_format($subtotal,2), 10, ' ', STR_PAD_LEFT) ."|\n";
        }
    }

    $txt = $txt . "+==========+=====+=====+=======+=====+==========+\n";
    $pajak =($total)*(10/100);
    $bayar =$total+$pajak;
    $txt =$txt."Total   :".str_pad(number_format($total,2),10, ' ', STR_PAD_LEFT)."\n";
    $txt =$txt."Pajak   :".str_pad(number_format($pajak,2), 10, ' ', STR_PAD_LEFT)."\n";
    $txt =$txt."Bayar   :".str_pad(number_format($bayar,2), 10, ' ', STR_PAD_LEFT)."\n";
    fwrite($myfile, $txt);
    fclose($myfile);
}
?>
<!DOCTYPE HTML>
<html>

<head>
    <style>
        body {
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            font-size: 12px
        }

        input {
            width: 80px;
        }

        .center {
            margin: auto;
            width: 50%;
            padding: 10px;
        }
    </style>
</head>

<body>
    <div class="center">
        <h1>BL STORE</h1>
        <?php
        if (isset($_POST["save"])) {
            save();
            header("location:struk.txt");
        }
        ?>
        <form action="" method="post">
            <table>
                <tr>
                    <th>ITEM</th>
                    <th>SIZE</th>
                    <th>QTY</th>
                    <th>DISC</th>


                </tr>
                <tr>
                    <td>
                        <select name="items[]" id="items">
                            <option value="Toshiba">Toshiba</option>
                            <option value="Samsung">Samsung</option>
                            <option value="Seagate">Seagete</option>

                        </select>
                    </td>
                    <td>
                        <select name="size[]" id="size">
                            <option value="1TB">1TB</option>
                            <option value="2TB">2TB</option>
                            <option value="4TB">4TB</option>

                        </select>
                    </td>
                    <td>
                        <input type="text" name="qty[]">
                    </td>
                    <td>
                        <input type="text" name="disc[]" value="0">
                    </td>
                </tr>
                <tr>
                    <td>
                        <select name="items[]" id="items">
                            <option value="Toshiba">Toshiba</option>
                            <option value="Samsung">Samsung</option>
                            <option value="Seagate">Seagete</option>

                        </select>
                    </td>
                    <td>
                        <select name="size[]" id="size">
                            <option value="1TB">1TB</option>
                            <option value="2TB">2TB</option>
                            <option value="4TB">4TB</option>

                        </select>
                    </td>
                    <td>
                        <input type="text" name="qty[]">
                    </td>
                    <td>
                        <input type="text" name="disc[]" value="0">
                    </td>
                </tr>
                <tr>
                    <td>
                        <select name="items[]" id="items">
                            <option value="Toshiba">Toshiba</option>
                            <option value="Samsung">Samsung</option>
                            <option value="Seagate">Seagete</option>

                        </select>
                    </td>
                    <td>
                        <select name="size[]" id="size">
                            <option value="1TB">1TB</option>
                            <option value="2TB">2TB</option>
                            <option value="4TB">4TB</option>

                        </select>
                    </td>
                    <td>
                        <input type="text" name="qty[]">
                    </td>
                    <td>
                        <input type="text" name="disc[]" value="0">
                    </td>
                </tr>
                <tr>
                    <td><input type="submit" name="save" value="Cetak">

                    </td>
                </tr>
            </table>

        </form>
    </div>
</body>

</html>
