import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.imageio.ImageIO;

public class photo_synthesis
{
    public static void jointPic(List<File> files, String newFileName)
    {
        try
        {
            BufferedImage[] imgs = new BufferedImage[files.size()];

            for (int i = 0; i < files.size(); i++)
            {
                imgs[i] = ImageIO.read(files.get(i));
            }

            BufferedImage imgNew = new BufferedImage(255, 255, BufferedImage.TYPE_INT_RGB);

            for (int i = 0; i < 255; i++)
            {
                for (int j = 0; j < 255; j++)
                {
                    int r0 = (imgs[0].getRGB(i,j) >> 16) & 0xFF;
                    int g0 = (imgs[0].getRGB(i,j) >> 8) & 0xFF;
                    int b0 = (imgs[0].getRGB(i,j) >> 0) & 0xFF;
                    int r1 = (imgs[1].getRGB(i,j) >> 16) & 0xFF;
                    int g1 = (imgs[1].getRGB(i,j) >> 8) & 0xFF;
                    int b1 = (imgs[1].getRGB(i,j) >> 0) & 0xFF;
                    System.out.println("("+(r0+r1)+","+(g0+g1)+","+(b0+b1)+")");
                    int red = r0+r1;
                    if(red > 255)
                    {
                        red = 0;
                    }
                    int green = g0+g1;
                    if(green > 255)
                    {
                        green = 0;
                    }
                    int blue = b0+b1;
                    if(blue > 255)
                    {
                        blue = 0;
                    }
                    int rgb=new Color(red,green,blue).getRGB();
                    imgNew.setRGB(i, j,rgb);
                }
            }

            File outFile = new File("C:/Users/User/Desktop/ctf/pic/" + newFileName);
            ImageIO.write(imgNew, "png", outFile);// 寫圖片
            System.out.println("===合併成功===");
        }
        catch (Exception e)
        {
            System.out.println("===合併失敗===");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws IOException
    {
        List<File> files = new ArrayList<>();
        String newFileName = "new.jpg";
        File file1 = new File("C:/Users/User/Desktop/ctf/pic/scrambled1.png");
        File file2 = new File("C:/Users/User/Desktop/ctf/pic/scrambled2.png");
        files.add(file1);
        files.add(file2);
        jointPic(files, newFileName);
    }
}
