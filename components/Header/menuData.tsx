import { Menu } from "@/types/menu";

const menuData: Menu[] = [
  {
    id: 1,
    title: "Home",
    path: "/",
    newTab: false,
  },
  {
    id: 2,
    title: "Product",
//     path: "/about",
    newTab: false,
    submenu: [
      {
        id: 21,
        title: "Product 1",
        path: "/about",
        newTab: false,
      },
      {
        id: 22,
        title: "Product 2",
        path: "/product/product2",
        newTab: false,
      },
      {
        id: 23,
        title: "Product 3",
        path: "/product/product3",
        newTab: false,
      }
      ]
  },
    {
    id: 3,
    title: "About",
    path: "/about",
    newTab: false,
  },
  {
    id: 4,
    title: "Pricing",
    path: "/blog",
    newTab: false,
  },
  {
    id: 5,
    title: "Contact",
    path: "/contact",
    newTab: false,
  },
  {
    id: 6,
    title: "Pages",
    newTab: false,
    submenu: [
      {
        id: 61,
        title: "About Page",
        path: "/about",
        newTab: false,
      },
      {
        id: 62,
        title: "Contact Page",
        path: "/contact",
        newTab: false,
      },
      {
        id: 63,
        title: "Blog Grid Page",
        path: "/blog",
        newTab: false,
      },
      {
        id: 64,
        title: "Blog Sidebar Page",
        path: "/blog-sidebar",
        newTab: false,
      },
      {
        id: 65,
        title: "Blog Details Page",
        path: "/blog-details",
        newTab: false,
      },
      {
        id: 66,
        title: "Sign In Page",
        path: "/signin",
        newTab: false,
      },
      {
        id: 67,
        title: "Sign Up Page",
        path: "/signup",
        newTab: false,
      },
      {
        id: 68,
        title: "Error Page",
        path: "/error",
        newTab: false,
      },
    ],
  },
];
export default menuData;
