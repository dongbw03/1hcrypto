declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"en": {
"news/2026-05-30-bitcoin-dip-buyers-place-500m-in-bids-as.md": {
	id: "news/2026-05-30-bitcoin-dip-buyers-place-500m-in-bids-as.md";
  slug: "news/2026-05-30-bitcoin-dip-buyers-place-500m-in-bids-as";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-bitcoin-plums-new-six-week-lows-as-analy.md": {
	id: "news/2026-05-30-bitcoin-plums-new-six-week-lows-as-analy.md";
  slug: "news/2026-05-30-bitcoin-plums-new-six-week-lows-as-analy";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-bitcoin-retail-sentiment-still-matters-s.md": {
	id: "news/2026-05-30-bitcoin-retail-sentiment-still-matters-s.md";
  slug: "news/2026-05-30-bitcoin-retail-sentiment-still-matters-s";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-cftc-backs-crypto-perpetual-contracts-is.md": {
	id: "news/2026-05-30-cftc-backs-crypto-perpetual-contracts-is.md";
  slug: "news/2026-05-30-cftc-backs-crypto-perpetual-contracts-is";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-coinbase-brings-global-crypto-derivative.md": {
	id: "news/2026-05-30-coinbase-brings-global-crypto-derivative.md";
  slug: "news/2026-05-30-coinbase-brings-global-crypto-derivative";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-extraordinarily-unusual-for-cftc-to-reve.md": {
	id: "news/2026-05-30-extraordinarily-unusual-for-cftc-to-reve.md";
  slug: "news/2026-05-30-extraordinarily-unusual-for-cftc-to-reve";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-sui-network-temporarily-stalls-again-aft.md": {
	id: "news/2026-05-30-sui-network-temporarily-stalls-again-aft.md";
  slug: "news/2026-05-30-sui-network-temporarily-stalls-again-aft";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-us-has-seized-nearly-1-billion-in-irania.md": {
	id: "news/2026-05-30-us-has-seized-nearly-1-billion-in-irania.md";
  slug: "news/2026-05-30-us-has-seized-nearly-1-billion-in-irania";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/2026-06-01-btc-etf-inflow.md": {
	id: "news/2026-06-01-btc-etf-inflow.md";
  slug: "news/2026-06-01-btc-etf-inflow";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
};
"zh": {
"news/2026-05-30-bitcoin-dip-buyers-place-500m-in-bids-as.md": {
	id: "news/2026-05-30-bitcoin-dip-buyers-place-500m-in-bids-as.md";
  slug: "news/2026-05-30-bitcoin-dip-buyers-place-500m-in-bids-as";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-bitcoin-plums-new-six-week-lows-as-analy.md": {
	id: "news/2026-05-30-bitcoin-plums-new-six-week-lows-as-analy.md";
  slug: "news/2026-05-30-bitcoin-plums-new-six-week-lows-as-analy";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-bitcoin-retail-sentiment-still-matters-s.md": {
	id: "news/2026-05-30-bitcoin-retail-sentiment-still-matters-s.md";
  slug: "news/2026-05-30-bitcoin-retail-sentiment-still-matters-s";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-cftc-backs-crypto-perpetual-contracts-is.md": {
	id: "news/2026-05-30-cftc-backs-crypto-perpetual-contracts-is.md";
  slug: "news/2026-05-30-cftc-backs-crypto-perpetual-contracts-is";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-coinbase-brings-global-crypto-derivative.md": {
	id: "news/2026-05-30-coinbase-brings-global-crypto-derivative.md";
  slug: "news/2026-05-30-coinbase-brings-global-crypto-derivative";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-extraordinarily-unusual-for-cftc-to-reve.md": {
	id: "news/2026-05-30-extraordinarily-unusual-for-cftc-to-reve.md";
  slug: "news/2026-05-30-extraordinarily-unusual-for-cftc-to-reve";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-sui-network-temporarily-stalls-again-aft.md": {
	id: "news/2026-05-30-sui-network-temporarily-stalls-again-aft.md";
  slug: "news/2026-05-30-sui-network-temporarily-stalls-again-aft";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-05-30-us-has-seized-nearly-1-billion-in-irania.md": {
	id: "news/2026-05-30-us-has-seized-nearly-1-billion-in-irania.md";
  slug: "news/2026-05-30-us-has-seized-nearly-1-billion-in-irania";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-06-01-btc-etf-inflow.md": {
	id: "news/2026-06-01-btc-etf-inflow.md";
  slug: "news/2026-06-01-btc-etf-inflow";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		"news": Record<string, {
  id: string;
  collection: "news";
  data: any;
}>;

	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = never;
}
